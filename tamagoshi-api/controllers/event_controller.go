package controllers

import (
	"context"
	"net/http"
	"time"

	"github.com/ekoinsight/ekoinsight/tamagoshi-api/configs"
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/models"
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/responses"

	"github.com/gin-gonic/gin"
	"github.com/go-playground/validator/v10"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
)

var eventCollection *mongo.Collection = configs.GetCollection(configs.DB, "events")
var validateEvent = validator.New()

func CreateEvent() gin.HandlerFunc {
	return func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		var event models.Event
		var ok bool
		defer cancel()
		eventData, existsFromCtx := c.Get("eventData")
		if !existsFromCtx {
			if err := c.BindJSON(&event); err != nil {
				c.AbortWithStatusJSON(http.StatusBadRequest, responses.EventResponse{Status: http.StatusBadRequest, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
				return
			}
		} else {
			event, ok = eventData.(models.Event)
			if !ok {
				c.AbortWithStatusJSON(http.StatusInternalServerError, gin.H{"error": "Invalid event data type"})
				return
			}
		}

		if validationErr := validateEvent.Struct(&event); validationErr != nil {
			c.AbortWithStatusJSON(http.StatusBadRequest, responses.EventResponse{Status: http.StatusBadRequest, Message: "error", Data: map[string]interface{}{"data": validationErr.Error()}})
			return
		}

		newEvent := models.Event{
			Id:        primitive.NewObjectID(),
			Type:      event.Type,
			UserId:    event.UserId,
			Score:     event.Score,
			Message:   event.Message,
			CreatedAt: primitive.NewDateTimeFromTime(time.Now()),
		}

		result, err := eventCollection.InsertOne(ctx, newEvent)
		if err != nil {
			c.AbortWithStatusJSON(http.StatusInternalServerError, responses.EventResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		c.AbortWithStatusJSON(http.StatusCreated, responses.EventResponse{Status: http.StatusCreated, Message: "success", Data: map[string]interface{}{"data": result}})
	}
}

func GetEvent() gin.HandlerFunc {
	return func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		eventId := c.Param("eventId")
		var event models.Event
		defer cancel()

		objId, _ := primitive.ObjectIDFromHex(eventId)

		err := eventCollection.FindOne(ctx, bson.M{"id": objId}).Decode(&event)
		if err != nil {
			c.AbortWithStatusJSON(http.StatusInternalServerError, responses.EventResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		c.AbortWithStatusJSON(http.StatusOK, responses.EventResponse{Status: http.StatusOK, Message: "success", Data: map[string]interface{}{"data": event}})
	}
}

func EditEvent() gin.HandlerFunc {
	return func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		eventId := c.Param("eventId")
		var event models.Event
		defer cancel()

		objId, _ := primitive.ObjectIDFromHex(eventId)

		//validateEvent the request body
		if err := c.BindJSON(&event); err != nil {
			c.AbortWithStatusJSON(http.StatusBadRequest, responses.EventResponse{Status: http.StatusBadRequest, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		//use the validator library to validateEvent required fields
		if validationErr := validateEvent.Struct(&event); validationErr != nil {
			c.AbortWithStatusJSON(http.StatusBadRequest, responses.EventResponse{Status: http.StatusBadRequest, Message: "error", Data: map[string]interface{}{"data": validationErr.Error()}})
			return
		}

		update := bson.M{"userId": event.UserId, "type": event.Type, "score": event.Score, "message": event.Message}
		result, err := eventCollection.UpdateOne(ctx, bson.M{"id": objId}, bson.M{"$set": update})

		if err != nil {
			c.AbortWithStatusJSON(http.StatusInternalServerError, responses.EventResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		//get updated event details
		var updatedEvent models.Event
		if result.MatchedCount == 1 {
			err := eventCollection.FindOne(ctx, bson.M{"id": objId}).Decode(&updatedEvent)
			if err != nil {
				c.AbortWithStatusJSON(http.StatusInternalServerError, responses.EventResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
				return
			}
		}

		c.AbortWithStatusJSON(http.StatusOK, responses.EventResponse{Status: http.StatusOK, Message: "success", Data: map[string]interface{}{"data": updatedEvent}})
	}
}

func DeleteEvent() gin.HandlerFunc {
	return func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		eventId := c.Param("eventId")
		defer cancel()

		objId, _ := primitive.ObjectIDFromHex(eventId)

		result, err := eventCollection.DeleteOne(ctx, bson.M{"id": objId})

		if err != nil {
			c.AbortWithStatusJSON(http.StatusInternalServerError, responses.EventResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		if result.DeletedCount < 1 {
			c.AbortWithStatusJSON(http.StatusNotFound,
				responses.EventResponse{Status: http.StatusNotFound, Message: "error", Data: map[string]interface{}{"data": "Event with specified ID not found!"}},
			)
			return
		}

		c.AbortWithStatusJSON(http.StatusOK,
			responses.EventResponse{Status: http.StatusOK, Message: "success", Data: map[string]interface{}{"data": "Event successfully deleted!"}},
		)
	}
}

func GetAllEvents() gin.HandlerFunc {
	return func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		var events []models.Event
		defer cancel()

		results, err := eventCollection.Find(ctx, bson.M{})

		if err != nil {
			c.AbortWithStatusJSON(http.StatusInternalServerError, responses.EventResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		//reading from the db in an optimal way
		defer results.Close(ctx)
		for results.Next(ctx) {
			var singleEvent models.Event
			if err = results.Decode(&singleEvent); err != nil {
				c.AbortWithStatusJSON(http.StatusInternalServerError, responses.EventResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			}

			events = append(events, singleEvent)
		}

		c.AbortWithStatusJSON(http.StatusOK,
			responses.EventResponse{Status: http.StatusOK, Message: "success", Data: map[string]interface{}{"data": events}},
		)
	}
}
