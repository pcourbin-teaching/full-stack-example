#!/bin/bash
#https://www.mokkapps.de/blog/how-to-generate-angular-and-spring-code-from-open-api-specification/
#https://github.com/nodejs/docker-node/blob/master/README.md#how-to-use-this-image
WORKDIR=/usr/src/app
DOCKER_IMAGE=timbru31/java-node:8-alpine
docker run -it --rm -v "$PWD":$WORKDIR -w $WORKDIR $DOCKER_IMAGE npm add @openapitools/openapi-generator-cli
docker run -it --rm -v "$PWD":$WORKDIR -w $WORKDIR $DOCKER_IMAGE npm run generate:api

# Change right of output folder
sudo chown -R $USER:$USER ./node_modules
sudo chown -R $USER:$USER ./openapi
