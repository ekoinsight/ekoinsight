package main

import (
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/configs"
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/routes" 
	"github.com/gin-contrib/cors"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	

	config := cors.DefaultConfig()
  config.AllowOrigins = []string{"https://*.ekoinsight.ca", "https://ekoinsight.ca"}

	router.Use(cors.New(config))

	//run database
	configs.ConnectDB()

	//routes
	routes.UserRoute(router)
	routes.EventRoute(router) //add this

	router.Run("0.0.0.0:8080")
}
