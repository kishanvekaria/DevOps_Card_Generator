#!/bin/bash
sudo chmod 666 /var/run/docker.sock

docker-compose down --rmi all
export DB_URI=${DB_URI} 
export SEC_KEY=${SEC_KEY} 
docker-compose build
sudo docker login
sudo docker-compose push