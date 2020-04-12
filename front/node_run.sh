#!/bin/bash
#./node_run.sh "npm install"
#https://openclassrooms.com/fr/courses/4668271-developpez-des-applications-web-avec-angular/5086918-installez-les-outils-et-creez-votre-projet
#ng generate component mon-premier
DOCKER_WORKDIR=/app
HOST_WORKDIR=DebatIDOFront
DOCKER_IMAGE=pcourbin/debatido_front:0.1.0
docker run -it --rm -v "$PWD/$HOST_WORKDIR":$DOCKER_WORKDIR -w $DOCKER_WORKDIR $DOCKER_IMAGE $1

# Change right of output folder
sudo chown -R $USER:$USER $PWD/$HOST_WORKDIR/
