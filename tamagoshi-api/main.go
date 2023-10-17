package main

import (
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/configs"
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/routes" 
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/middlewares"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	router.Use(middlewares.VerifyToken())

	//run database
	configs.ConnectDB()

	//routes
	routes.UserRoute(router)
	routes.EventRoute(router) //add this

	router.Run("0.0.0.0:8080")
}
