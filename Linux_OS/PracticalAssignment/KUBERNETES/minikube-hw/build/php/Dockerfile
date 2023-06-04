FROM php:8.1-apache
WORKDIR /var/www/html

COPY ./app/index.php index.php
# COPY src/ src
EXPOSE 80
RUN apt-get update && \
    docker-php-ext-install mysqli pdo pdo_mysql \
RUN apt install vim -y
