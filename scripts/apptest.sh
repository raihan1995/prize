#!/bin/bash
#check the pathway
pwd
#check whats inside the folder
ls

#install all dependencies
sudo apt-get update
sudo apt-get install -y python3-venv python3.pip

#cd to service1, install dependencies and run pytest cov
cd service1
pip3 install -r requirements.txt
python3 -m pytest --cov app

#same for service 2
cd ../service2

python3 -m pytest --cov app

#same for service 3
cd ../service3
python3 -m pytest --cov app

#same for service 4
cd ../service4
python3 -m pytest --cov app

#return to the start and deacativate
deactivate
cd ..