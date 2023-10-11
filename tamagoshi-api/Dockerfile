# Stage 1: Build
FROM golang:1.21.3-alpine3.18 AS build
WORKDIR /app
COPY . .
RUN go mod download
RUN go build

# Stage 2: Final Image
FROM alpine:latest
WORKDIR /app
COPY --from=build /app/tamagoshi-api .
EXPOSE 8080
CMD ["./tamagoshi-api"]
