#!/bin/bash
<< EOF
scp /home/jenkins/.jenkins/workspace/project2pipeline/docker-compose.yaml jenkins@35.233.174.240:docker-compose.yaml
ssh 35.233.174.240
export SEC_KEY=${SEC_KEY} 
export DB_URI=${DB_URI} 
docker stack deploy --compose-file docker-compose.yaml cardgen
EOF