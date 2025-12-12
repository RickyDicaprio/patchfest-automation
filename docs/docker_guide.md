# Docker Guide

## Introduction
- Why Docker is used in this project.
- Overview of the containers and images.

## Prerequisites
- Install Docker & Docker Compose.

## Project Structure
- Location of Dockerfiles.
- Explanation of docker-compose.yml.

## Building Containers
- docker build -t project-name .

## Running Containers
    ```bash
    docker run -p 8080:8080 project-name

# Using Docker Compose
    ```bash
    docker compose up --build
    docker compose down
# Development vs Production Containers
    --> Differences in configuration.
# Working with Volumes, Networks, and Logs
    --> How persistent data is handled.
    --> Viewing container logs.
# Debugging
    --> Exec into a running container:
        ```bash
        docker exec -it container-name /bin/sh
# Best Practices
    --> Keeping images small.
    --> Using .dockerignore.




