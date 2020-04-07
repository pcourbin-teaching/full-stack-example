#!/bin/bash
#set -ev
openapi_file="openapi-debatsido.yaml"
out_framework="python-flask"
package_name="DebatIDOAPI"

openapi_file=${1:-$openapi_file}
out_framework=${2:-$out_framework}
package_name=${3:-$package_name}

docker run --rm \
      -v ${PWD}:/local openapitools/openapi-generator-cli generate \
      -i /local/$openapi_file \
      -g $out_framework \
      --package-name $package_name \
      -o /local/$package_name

# Change right of output folder
sudo chown -R $USER:$USER ./$package_name
