# Stage 1: Build
FROM golang:1.21 AS build
WORKDIR /app
COPY . .
RUN go mod download
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o tamagoshi-api

# Stage 2: Final Image
FROM alpine:latest
WORKDIR /app
COPY --from=build /app/tamagoshi-api .
EXPOSE 8080
CMD ["./tamagoshi-api"]
