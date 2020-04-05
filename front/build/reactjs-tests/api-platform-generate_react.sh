#!/bin/sh

#https://api-platform.com/docs/client-generator/react/
#https://github.com/api-platform/client-generator

set -e
if [ -z "$API_SCHEME" ]; then
  API_SCHEME_TEMP="http"
else
  API_SCHEME_TEMP=$API_SCHEME
fi

if [ -z "$API_HOST" ]; then
  # If not defined, get DOCKER HOST IP
  API_HOST_TEMP=$(/sbin/ip route|awk '/default/ { print $3 }')
else
  API_HOST_TEMP=$API_HOST
fi

if [ -z "$API_PORT" ]; then
  API_PORT_TEMP="3000"
else
  API_PORT_TEMP=$API_PORT
fi

if [ -z "$API_PATH" ]; then
  API_PATH_TEMP="/api"
else
  API_PATH_TEMP=$API_PATH
fi

npx @api-platform/client-generator $API_SCHEME_TEMP://$API_HOST_TEMP:$API_PORT_TEMP$API_PATH_TEMP ./src --resource protagonist --format openapi2

ls -Al ./src
