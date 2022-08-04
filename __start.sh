#!/bin/bash
########################
# Legacy Code: 
# Author: David Baldwin
# Reviewer: David Baldwin
# Last Reviewed: Aug 4, 2022
# Last Updated:  Aug 4, 2022
# Reason for deprecation:
#         this script is no longer needed to build or run the application now that
#         we are using docker
###################
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
