#!/bin/bash
#set -ev
#https://pypi.org/project/sqlacodegen/
#https://github.com/zalando/connexion/blob/master/examples/openapi3/sqlalchemy/orm.py
DOCKER_WORKDIR=/usr/src/app
HOST_WORKDIR=debatsido
DOCKER_IMAGE=python:2-alpine
#pip install sqlacodegen
#pip install pymysql
#sqlacodegen mysql+pymysql://user:password@localhost/debatsido > sqlalchemy_database_model.py
docker run -it --rm -v "$PWD/$HOST_WORKDIR":$DOCKER_WORKDIR -w $DOCKER_WORKDIR $DOCKER_IMAGE "pip install sqlacodegen && sqlacodegen mysql+pymysql://user:password@localhost/dbname"

# Change right of output folder
sudo chown -R $USER:$USER $PWD/$HOST_WORKDIR/
