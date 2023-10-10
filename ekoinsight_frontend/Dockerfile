FROM node:20 as build
WORKDIR /usr/app
COPY . /usr/app
RUN npm install
RUN npm run build

FROM nginx:1.23.1-alpine
EXPOSE 80
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /usr/app/build /usr/share/nginx/html
