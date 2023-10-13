package models

import "go.mongodb.org/mongo-driver/bson/primitive"

type User struct {
	Id     primitive.ObjectID `json:"id,omitempty" validate:"required"`
	Name   string             `json:"name,omitempty" validate:"required"`
	Mail   string             `json:"mail,omitempty" validate:"required"`
	Health int                `json:"health,omitempty"`
}
