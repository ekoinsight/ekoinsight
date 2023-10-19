package routes

import (
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/controllers"
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/middlewares"

	"github.com/gin-gonic/gin"
)

func UserRoute(router *gin.Engine) {
	router.OPTIONS("/user/:userId/feed", controllers.OptionsFeedUser())
	router.Use(middlewares.VerifyToken())

	router.POST("/user", controllers.CreateUser())
	router.GET("/user/:userId", controllers.GetUser())
	router.PUT("/user/:userId", controllers.EditUser())
	
	router.POST("/user/:userId/feed", controllers.FeedUser())
	router.GET("/users", controllers.GetAllUsers())

	
	router.DELETE("/user/:userId", controllers.DeleteUser())
}


