# Dockerize
You can build the image and container with just one script:
1. cd system-two
2. ./dockerize.sh

# Build docker image
1. cd system-two
2. sudo docker build -t system-two-image .

# Run docker container
1. cd system-two
2. sudo docker run -it -p 5002:5002 --name system-two-container system-two-image

# Swagger
http://0.0.0.0:5002

# Endponts
url: http://0.0.0.0:5002/score/cpfNumber
description: returns the score of a valid user.
obs.: 
- All valid cpfs are going to return the same mocked user infos.
- The user score return aways 500.

# Run tests
1. cd system-two
2. python -m unittest unitTest/ValidationsUnitTest.py

