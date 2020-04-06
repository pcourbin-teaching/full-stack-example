#!/bin/bash
#./node_run.sh "npm install ng-swagger-gen --save-dev" debatsido
#./node_run.sh "debatsido/node_modules/.bin/ng-swagger-gen -i ./openapi-debatsido-v2.yaml -o debatsido/api"

#./node_run.sh "npm install ng-openapi-gen --save-dev" debatsido
#./node_run.sh "debatsido/node_modules/.bin/ng-openapi-gen --input ./openapi-debatsido-v3.yaml --output debatsido/api3"
WORKDIR=/usr/src/app
DOCKER_IMAGE=timbru31/java-node:8-alpine
if  [[ ! -z "$2" ]]
then
  cd $2
fi
# npx ng new debatsido
docker run -it --rm -v "$PWD":$WORKDIR -w $WORKDIR $DOCKER_IMAGE $1
