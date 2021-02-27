#!/bin/bash
ssh 35.233.174.240 << EOF
scp /home/jenkins/.jenkins/workspace/project2pipeline/docker-compose.yaml /home/jenkins/
export SEC_KEY=${SEC_KEY} 
export DB_URI=${DB_URI} 
docker stack deploy --compose-file docker-compose.yaml cardgen
EOF