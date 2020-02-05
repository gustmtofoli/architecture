FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
# COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install flask
RUN pip3 install flask-rest
RUN pip3 install flask-restplus
RUN pip3 install validate_docbr
RUN pip3 install flask-api

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]

EXPOSE 5003