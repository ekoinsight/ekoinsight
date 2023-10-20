package models

type User struct {
	Id     string 						`json:"id,omitempty" validate:"required"`
	Name   string             `json:"name,omitempty" validate:"required"`
	Mail   string             `json:"mail,omitempty" validate:"required"`
	Health int             	  	`json:"health,omitempty" validate:"required"`
}
