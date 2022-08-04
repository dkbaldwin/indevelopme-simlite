#!/bin/bash

#variables
image_name="simcontainer-image"
external_port="8000"
internal_port="80"
container_name="simcontainer"


#build the image
docker build -t ${image_name} .
################################
#todo: need to create docker-compose.yml
# file to remove the need of the following lines
################################

#stop the old container
docker stop ${container_name}
#delete the old container
docker rm ${container_name}
#create a new container
docker run -d -p ${external_port}:${internal_port} \
  --name=${container_name} ${image_name}
  #  -v $PWD:/app \
