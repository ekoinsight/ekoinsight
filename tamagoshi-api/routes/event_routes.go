package routes

import (
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/controllers"

	"github.com/gin-gonic/gin"
)

func EventRoute(router *gin.Engine) {
	router.POST("/event", controllers.CreateEvent())
	router.GET("/event/:eventId", controllers.GetEvent())
	router.PUT("/event/:eventId", controllers.EditEvent())
	router.DELETE("/event/:eventId", controllers.DeleteEvent())
	router.GET("/events", controllers.GetAllEvents())
}
