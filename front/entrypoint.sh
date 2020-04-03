#!/bin/bash
react_env_file=${APP_HOME}/.env
sed -i -e "s|API_URL = .*$|API_URL = \'"${API_URL}"\'|" ${react_env_file}

cd ${APP_HOME}
npm start
