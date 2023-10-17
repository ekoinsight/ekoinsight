package middlewares

import (
	"context"
	"net/http"

	"github.com/ekoinsight/ekoinsight/tamagoshi-api/configs"
	"github.com/ekoinsight/ekoinsight/tamagoshi-api/responses"

	"github.com/gin-gonic/gin"
	"google.golang.org/api/idtoken"
)


func VerifyToken() gin.HandlerFunc {
	return func(c *gin.Context) {
		idToken := c.GetHeader("Authorization")
		if idToken == "" {
			c.AbortWithStatusJSON(http.StatusUnauthorized, responses.EventResponse{Status: http.StatusUnauthorized, Message: "Unauthorized", Data: map[string]interface{}{"data": "StatusUnauthorized"}})
			return
		}
		tokenContent, err := idtoken.Validate(context.Background(), idToken, configs.EnvOIDCAudience())
		if err != nil {
			c.AbortWithStatusJSON(http.StatusForbidden, responses.EventResponse{Status: http.StatusForbidden, Message: "Invalid token", Data: map[string]interface{}{"data": err.Error()}})
			return
		}
		c.Set("tokenContent", tokenContent)
		c.Next()
	}
}