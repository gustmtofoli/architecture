# Dockerize
You can build the image and container with just one script:
1. cd system-one
2. ./dockerize.sh

# Build docker image
1. cd system-one
2. sudo docker build -t system-one-image .

# Run docker container
1. cd system-one
2. sudo docker run -it -p 5001:5001 --name system-one-container system-one-image

# Swagger
http://0.0.0.0:5001

# Endponts
url: http://0.0.0.0:5001/info/cpfNumber
description: returns information of a valid user.
obs.: 
- All valid cpfs are going to return the same mocked user infos: name, cpf, address and debtList.

# Run tests
1. cd system-one
2. python -m unittest unitTest/ValidationsUnitTest.py

