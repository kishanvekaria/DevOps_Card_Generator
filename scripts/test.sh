#!/bin/bash
pwd

cd ./service1
pip3 install -r requirements.txt
python3 -m pytest --cov app 
cd ..

cd ./service2
python3 -m pytest --cov app
cd ..

cd ./service3
python3 -m pytest --cov app
cd ..

cd ./service4
python3 -m pytest --cov app
cd ..