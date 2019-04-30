#!/bin/sh

SERVER_MANAGER_PATH="$INSTALL_PATH/plugins/server-manager"
NEW_UUID=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

cd /opt/server-manager/linux

if [ ! -d $SERVER_MANAGER_PATH ]; then
  sed -i "
    s/  username:.*/  username:/
    s/  password:.*/  password:/
    s/  install_path:.*/  install_path: ${AC_FOLDER}/
    s/  hostname:.*/  hostname: 0.0.0.0:${SM_HTTP_PORT}/
    s/  session_key:.*/  session_key: ${NEW_UUID}/
  " config.yml
  cp -rf . $SERVER_MANAGER_PATH
fi
