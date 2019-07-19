#!/bin/sh
mkdir -p /usr/local/research35

echo copy files...
echo startup...

# stop docker 
sudo docker stop research35.db
sudo docker stop research35.web
# rm docker 
sudo docker rm research35.db
sudo docker rm research35.web
# run docker 
sudo docker run --name=research35.db -p 0.0.0.0:27017:27017 -v /usr/local/research35/data/db:/data/db -d mongo
sudo docker run --name=research35.web --link=research35.db -d -p 0.0.0.0:80:80 bowen/research35.web 'python3' '/usr/local/research35/web/manage.py' 'runserver' '0.0.0.0:80'
