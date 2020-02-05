#!/bin/bash
set -e

echo
echo "We are going to build System 2."
echo
echo "It can take some time..."
echo

SYSTEM_NAME="system-two"
IMAGE_NAME="$SYSTEM_NAME-image"
CONTAINER_NAME="$SYSTEM_NAME-container"

sudo docker build -t "$IMAGE_NAME" .

echo

sudo docker run -it -p 5002:5002 --name "$CONTAINER_NAME" "$IMAGE_NAME"