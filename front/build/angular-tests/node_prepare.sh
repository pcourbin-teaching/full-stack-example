#!/bin/bash
#https://openclassrooms.com/fr/courses/4668271-developpez-des-applications-web-avec-angular/5086918-installez-les-outils-et-creez-votre-projet
WORKDIR=/usr/src/app
DOCKER_IMAGE=timbru31/java-node:8-alpine
docker run -it --rm -v "$PWD":$WORKDIR -w $WORKDIR $DOCKER_IMAGE npm install @angular/cli

# Change right of output folder
sudo chown -R $USER:$USER ./node_modules
