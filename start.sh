#!/bin/bash

#variables
image_name="simcontainer-image"
external_port="8000"
internal_port="80"
container_name="simcontainer"


docker build -t ${image_name} .
docker build -t  .
docker run -d -p ${external_port}:${internal_port} \
  --name=${container_name} ${image_name}
  #  -v $PWD:/app \
