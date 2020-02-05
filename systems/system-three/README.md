# Dockerize
You can build the image and container with just one script:
1. cd system-three
2. ./dockerize.sh

# Build docker image
1. cd system-three
2. sudo docker build -t system-three-image .

# Run docker container
1. cd system-three
2. sudo docker run -it -p 5003:5003 --name system-three-container system-three-image

# Swagger
http://0.0.0.0:5003

# Endponts
url: http://0.0.0.0:5003/events/cpfNumber
description: returns the last event of a valid user.
obs.: 
- All valid cpfs are going to return the same mocked user infos.

# Run tests
1. cd system-three
2. python -m unittest unitTest/ValidationsUnitTest.py

