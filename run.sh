#!/bin/bash

# Function to remove the container if it exists
remove_container_if_exists() {
    container_name=$1
    if [ "$(docker ps -a -q -f name=$container_name)" ]; then
        echo "Removing existing container: $container_name"
        docker rm -f $container_name
    fi
}

# Define your container names here
containers=("zookeeper-server" "kafka-server")

# Remove containers if they exist
for container in "${containers[@]}"; do
    remove_container_if_exists "$container"
done

# Start the containers with docker-compose
docker-compose up -d
