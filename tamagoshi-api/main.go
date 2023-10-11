package main

import (
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/configs"
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/routes" //add this

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	//run database
	configs.ConnectDB()

	//routes
	routes.UserRoute(router)
	routes.EventRoute(router) //add this

	router.Run("0.0.0.0:8080")
}
