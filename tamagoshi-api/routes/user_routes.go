package routes

import (
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/controllers"
	"github.com/gin-gonic/gin"
)

func UserRoute(router *gin.Engine) {
	router.POST("/user", controllers.CreateUser())
	router.GET("/user/:userId", controllers.GetUser())
	router.PUT("/user/:userId", controllers.EditUser())
	router.DELETE("/user/:userId", controllers.DeleteUser())
	router.POST("/user/:userId/feed", controllers.FeedUser())
	router.OPTIONS("/user/:userId/feed", controllers.OptionsFeedUser())
	router.GET("/users", controllers.GetAllUsers())
}
