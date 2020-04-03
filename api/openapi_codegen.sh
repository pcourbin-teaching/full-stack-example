#!/bin/bash

#set -ev
openapi_file="./debatido.yaml"
out_framework="python-flask"
package_name="DebatIDOAPI"

openapi_file=${1:-$openapi_file}
out_framework=${2:-$out_framework}
package_name=${3:-$package_name}

mkdir -p ./out/$package_name-$out_framework
docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3:3.0.19 generate \
    -i /local/$openapi_file \
    -l $out_framework \
    -DpackageName=$package_name \
    -o /local/out/$package_name-$out_framework

# Change right of output folder
sudo chown -R $USER:$USER ./out

# If "python-fask" add package "connexion[swagger-ui]" to the requirements (install the Swagger GUI)
#if [ "$out_framework" = "python-flask" ]; then
  #echo "swagger-ui-bundle" >> ./out/$package_name-$out_framework/requirements.txt
#fi
