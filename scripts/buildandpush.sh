#!/bin/bash
sudo chmod 666 /var/run/docker.sock

docker-compose down --rmi all
docker-compose build
sudo docker login
export DB_URI=${DB_URI} 
export SEC_KEY=${SEC_KEY} 
sudo docker-compose push