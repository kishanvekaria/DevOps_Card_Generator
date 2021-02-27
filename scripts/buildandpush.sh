#!/bin/bash
sudo chmod 666 /var/run/docker.sock

docker-compose down --rmi all 
docker-compose build
sudo docker login
echo ${DB_URI}
echo $(SEC_KEY)
sudo docker-compose push