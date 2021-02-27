#!/bin/bash

scp -i ./ssh/id_rsa /home/jenkins/.jenkins/workspace/project2pipeline/docker-compose.yaml jenkins@35.233.174.240:docker-compose.yaml
ssh -i ./ssh/id_rsa jenkins@35.233.174.240 << EOF
export SEC_KEY=${SEC_KEY} 
export DB_URI=${DB_URI} 
docker stack deploy --compose-file docker-compose.yaml cardgen
EOF