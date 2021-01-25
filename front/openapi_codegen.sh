#!/bin/bash
#set -ev
openapi_file="../api/openapi-spot.yaml"
out_framework="typescript-angular"
package_name="SPOTAPI"

openapi_file=${1:-$openapi_file}
out_framework=${2:-$out_framework}
package_name=${3:-$package_name}

cp $openapi_file ./openapi.temp.yaml
docker run --rm \
      -v ${PWD}:/local openapitools/openapi-generator-cli generate \
      -i /local/openapi.temp.yaml \
      -g $out_framework \
      --package-name $package_name \
      -o /local/SPOTFront/$package_name

rm ./openapi.temp.yaml
# Change right of output folder
sudo chown -R $USER:$USER ./SPOTFront
