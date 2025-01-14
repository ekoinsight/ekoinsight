package controllers

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"mime/multipart"
	"net/http"
	"os"
	"time"
	"encoding/json"

	"github.com/ekoinsight/ekoinsight/tamagoshi-api/configs"
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/models"
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/responses"

	"github.com/gin-gonic/gin"
	"github.com/go-playground/validator/v10"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"google.golang.org/api/idtoken"
)

var userCollection *mongo.Collection = configs.GetCollection(configs.DB, "users")
var validateUser = validator.New()

func CreateUser() gin.HandlerFunc {
	return func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		var user models.User
		defer cancel()

		//validateUser the request body
		if err := c.BindJSON(&user); err != nil {
			c.JSON(http.StatusBadRequest, responses.UserResponse{Status: http.StatusBadRequest, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		//use the validator library to validateUser required fields
		if validationErr := validateUser.Struct(&user); validationErr != nil {
			c.JSON(http.StatusBadRequest, responses.UserResponse{Status: http.StatusBadRequest, Message: "error", Data: map[string]interface{}{"data": validationErr.Error()}})
			return
		}

		newUser := models.User{
			Id:   user.Id,
			Name: user.Name,
			Mail: user.Mail,
		}
		errFindOne := userCollection.FindOne(ctx, bson.M{"id": user.Id}).Decode(&user)
		if errFindOne != nil && errFindOne != mongo.ErrNoDocuments {
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": errFindOne.Error()}})
			return
		} else if errFindOne == nil {
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": fmt.Errorf("User %v already exists")}})
			return
		}
		
		result, err := userCollection.InsertOne(ctx, newUser)
		if err != nil {
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		c.JSON(http.StatusCreated, responses.UserResponse{Status: http.StatusCreated, Message: "success", Data: map[string]interface{}{"data": result}})
	}
}

func GetUser() gin.HandlerFunc {
	return func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)

		userId := c.Param("userId")
		var user models.User
		defer cancel()
		err := userCollection.FindOne(ctx, bson.M{"id": userId}).Decode(&user)
		if err != nil {
			if err == mongo.ErrNoDocuments {
				log.Printf("Error ErrNoDocuments : %s", err.Error())
				err = nil
				defer cancel()
				tokenData := c.MustGet("tokenContent")
				token, ok := tokenData.(*idtoken.Payload)
				if !ok {
					c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
					return
				} else {
					var name, email, sub string
					if value, ok := token.Claims["sub"].(string); ok {
						sub = value
					}
					if value, ok := token.Claims["name"].(string); ok {
						name = value
					}
					if value, ok := token.Claims["email"].(string); ok {
						// 'value' is now the extracted string
						email = value
					}

					newUser := models.User{
						Id:   sub,
						Name: name,
						Mail: email,
					}
					_, err := userCollection.InsertOne(ctx, newUser)
					if err != nil {
						c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
						return
					}
					log.Printf("User succesfully created : %v", user)
					err = userCollection.FindOne(ctx, bson.M{"id": userId}).Decode(&user)
					if err != nil {
						c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
						return
					}
					health, err := UserHealth(userId)
					
					if err != nil {
						c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
						return 
					}
					user.Health = health
					log.Printf("Updater user with computed health : %v", user)
					c.JSON(http.StatusOK, responses.UserResponse{Status: http.StatusOK, Message: "success", Data: map[string]interface{}{"data": user}})
					return
				}
			}
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		log.Printf("User sucesfsfully found : %v", user)
		health, err := UserHealth(userId)
		if err != nil {
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return 
		}
		user.Health = health
		log.Printf("Updater user with computed health : %v", user)
		c.JSON(http.StatusOK, responses.UserResponse{Status: http.StatusOK, Message: "success", Data: map[string]interface{}{"data": user}})
	}
}

func UserHealth(id string) (int, error) {
	log.Printf("Compute health of user : %s", id)
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	var events []models.Event
	defer cancel()

	
	// Lookup all Feed events of user (id) in the last 48 hours
	filter := bson.M{
		"userid": id,
		"type": "Feed",
		"createdat": bson.M{
			"$gte": primitive.NewDateTimeFromTime(time.Now().Add(-48 * time.Hour)),
		},
	}
	results, err := eventCollection.Find(ctx, filter)
	if err != nil {
		return -1, err
	}
	//reading from the db in an optimal way
	defer results.Close(ctx)
	for results.Next(ctx) {
		var singleEvent models.Event
		if err = results.Decode(&singleEvent); err != nil {
			return -1, err
		}

		events = append(events, singleEvent)
	}
	log.Printf("Found %v feed event in the last 48h for user : %v", len(events),id)
	userScore := 0
	if err != nil {
		return -1, err
	}
	for _, event := range events {
		log.Printf("Computing event %v with score: %v", event.Message, event.Score)
		userScore += event.Score
	}
	log.Printf("User score computed: %v", userScore)
	if userScore < 0 {
		log.Printf("Correct score to zero: %v", userScore)
		userScore = 0
	}
	return userScore, nil
} 

func EditUser() gin.HandlerFunc {
	return func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		userId := c.Param("userId")
		var user models.User
		defer cancel()

		//validateUser the request body
		if err := c.BindJSON(&user); err != nil {
			c.JSON(http.StatusBadRequest, responses.UserResponse{Status: http.StatusBadRequest, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		//use the validator library to validateUser required fields
		if validationErr := validateUser.Struct(&user); validationErr != nil {
			c.JSON(http.StatusBadRequest, responses.UserResponse{Status: http.StatusBadRequest, Message: "error", Data: map[string]interface{}{"data": validationErr.Error()}})
			return
		}

		update := bson.M{"name": user.Name, "mail": user.Mail}
		result, err := userCollection.UpdateOne(ctx, bson.M{"id": userId}, bson.M{"$set": update})

		if err != nil {
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		//get updated user details
		var updatedUser models.User
		if result.MatchedCount == 1 {
			err := userCollection.FindOne(ctx, bson.M{"id": userId}).Decode(&updatedUser)
			if err != nil {
				c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
				return
			}
		}

		c.JSON(http.StatusOK, responses.UserResponse{Status: http.StatusOK, Message: "success", Data: map[string]interface{}{"data": updatedUser}})
	}
}

func DeleteUser() gin.HandlerFunc {
	return func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		userId := c.Param("userId")
		defer cancel()
		result, err := userCollection.DeleteOne(ctx, bson.M{"id": userId})

		if err != nil {
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		if result.DeletedCount < 1 {
			c.JSON(http.StatusNotFound,
				responses.UserResponse{Status: http.StatusNotFound, Message: "error", Data: map[string]interface{}{"data": "User with specified ID not found!"}},
			)
			return
		}

		c.JSON(http.StatusOK,
			responses.UserResponse{Status: http.StatusOK, Message: "success", Data: map[string]interface{}{"data": "User successfully deleted!"}},
		)
	}
}

func GetAllUsers() gin.HandlerFunc {
	return func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		var users []models.User
		defer cancel()

		results, err := userCollection.Find(ctx, bson.M{})

		if err != nil {
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		//reading from the db in an optimal way
		defer results.Close(ctx)
		for results.Next(ctx) {
			var singleUser models.User
			if err = results.Decode(&singleUser); err != nil {
				c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			}

			users = append(users, singleUser)
		}

		c.JSON(http.StatusOK,
			responses.UserResponse{Status: http.StatusOK, Message: "success", Data: map[string]interface{}{"data": users}},
		)
	}
}

type FeedEventStruct struct {
	Score int `json:"score,omitempty"`
	Reaction string `json:"reaction,omitempty"`
}

func FeedUser() gin.HandlerFunc {
	return func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		userId := c.Param("userId")
		var user models.User
		defer cancel()

		err := userCollection.FindOne(ctx, bson.M{"id": userId}).Decode(&user)
		if err != nil {
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		err = c.Request.ParseMultipartForm(100 * 1024 * 1024)
		if err != nil {
			log.Printf("Error ParseMultipartForm : %s", err.Error())
			c.JSON(http.StatusBadRequest, responses.UserResponse{Status: http.StatusBadRequest, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		file, header, err := c.Request.FormFile("file")
		if err != nil {
			log.Printf("Error retrieving file from request: %s", err.Error())
			c.JSON(http.StatusBadRequest, responses.UserResponse{Status: http.StatusBadRequest, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		defer file.Close()
		log.Printf("File uploaded: %s (Size: %d bytes)", header.Filename, header.Size)
		uploadDir := "uploads"
		if _, err := os.Stat(uploadDir); os.IsNotExist(err) {
			err = os.MkdirAll(uploadDir, os.ModePerm)
			if err != nil {
				log.Printf("Error creating upload folder: %s", err.Error())
				c.JSON(http.StatusBadRequest, responses.UserResponse{Status: http.StatusBadRequest, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
				return
			}
		}

		out, err := os.Create("uploads/" + header.Filename)
		if err != nil {
			log.Printf("Error creating file: %s", err.Error())
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		defer out.Close()

		// Copy the file data to the new file
		_, err = io.Copy(out, file)
		if err != nil {
			log.Printf("Error copying file data: %s", err.Error())
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		// TODO query backend to determine feed score

		file, err = os.Open("uploads/" + header.Filename)
		if err != nil {
			log.Printf("Error opening file: %s", err.Error())
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		defer file.Close()

		body := &bytes.Buffer{}
		writer := multipart.NewWriter(body)
		part, err := writer.CreateFormFile("file", "uploads/"+header.Filename)
		if err != nil {
			log.Printf("Error closing create buffer from file: %s", err.Error())
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		_, err = io.Copy(part, file)
		if err != nil {
			log.Printf("Error closing reader file: %s", err.Error())
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		err = writer.Close()
		if err != nil {
			log.Printf("Error closing reader file: %s", err.Error())
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		req, err := http.NewRequest("POST", fmt.Sprintf("%v/feed", configs.EnvBackendUrl()), body)
		if err != nil {
			log.Printf("Error creating request to ekoinsight backend API: %s", err.Error())
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		req.Header.Set("Content-Type", writer.FormDataContentType())
		log.Printf("Send request %v to backend: %s", req.Header, configs.EnvBackendUrl())
		client := &http.Client{}

		resp, err := client.Do(req)
		if err != nil {
			log.Printf("Error querying to ekoinsight backend API: %s", err.Error())
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		defer resp.Body.Close()

		if resp.StatusCode != http.StatusOK {
			log.Printf("Error from ekoinsight backend API: status not ok")
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		responseBody, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			log.Printf("Error reading backend body content: %s", err.Error())
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}


		var feedEventResp FeedEventStruct

		// Unmarshal the JSON into your struct
		err = json.Unmarshal(responseBody, &feedEventResp)
		if err != nil {
			log.Printf("Error unmarshalling backend body content: %s", err.Error())
			c.JSON(http.StatusInternalServerError, responses.UserResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		// Log the response body
		log.Printf("API Response Body: %s", string(responseBody))

		feedEvent := models.Event{
			Type:      "Feed",
			UserId:    userId,
			Score:     feedEventResp.Score,
			Message:   feedEventResp.Reaction,
			CreatedAt: primitive.NewDateTimeFromTime(time.Now()),
		}
		c.Set("eventData", feedEvent)
		eventHandler := CreateEvent()
		eventHandler(c)
	}
}

func OptionsFeedUser() gin.HandlerFunc {
	return func(c *gin.Context) {
		c.Header("Access-Control-Allow-Origin", "*")
		c.Header("Access-Control-Allow-Methods", "POST, OPTIONS")
		c.Header("Access-Control-Allow-Headers", "Content-Type, Authorization")
		// Respond with no content for OPTIONS request
		c.Status(http.StatusNoContent)
		return
	}
}
