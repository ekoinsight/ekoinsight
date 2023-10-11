package models

import "go.mongodb.org/mongo-driver/bson/primitive"

type Event struct {
	Id        primitive.ObjectID `json:"id,omitempty"`
	Type      string             `json:"type,omitempty"`
	UserId    string             `json:"userId,omitempty" validate:"required"`
	Score     int                `json:"score,omitempty" validate:"required"`
	Message   string             `json:"message,omitempty" validate:"required"`
	CreatedAt primitive.DateTime `json:"created_at,omitempty" validate:"required"`
}

//
