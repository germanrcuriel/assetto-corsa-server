#!/bin/sh

SERVER_MANAGER_PATH="$INSTALL_PATH/plugins/server-manager"
NEW_UUID=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

cd /opt/server-manager/linux

if [ ! -d $SERVER_MANAGER_PATH ]; then
  sed -i "
    s/  type:.*/  type: json/
    s/  username:.*/  username:/
    s/  password:.*/  password:/
    s#  install_path:.*#  install_path: ${INSTALL_PATH}#
    s/  hostname:.*/  hostname: 0.0.0.0:${SM_HTTP_PORT}/
    s/  session_key:.*/  session_key: ${NEW_UUID}/
  " config.yml
  cp -rf . $SERVER_MANAGER_PATH

    mkdir -p $SERVER_MANAGER_PATH/server_manager.db
  cat >> $SERVER_MANAGER_PATH/server_manager.db/server_options.json <<EOL
{
  "Name": "${AC_SERVER_NAME}",
  "Password": "${AC_PASSWORD}",
  "AdminPassword": "${AC_ADMIN_PASSWORD}",
  "UDPPort": ${AC_UDP_PORT},
  "TCPPort": ${AC_TCP_PORT},
  "HTTPPort": ${AC_HTTP_PORT},
  "UDPPluginLocalPort": ${AC_PLUGIN_LOCAL_PORT},
  "UDPPluginAddress": "127.0.0.1:${AC_PLUGIN_ADDRESS_LOCAL_PORT}",
  "AuthPluginAddress": "",
  "RegisterToLobby": 1,
  "ClientSendIntervalInHertz": 18,
  "SendBufferSize": 0,
  "ReceiveBufferSize": 0,
  "KickQuorum": 85,
  "VotingQuorum": 80,
  "VoteDuration": 20,
  "BlacklistMode": 1,
  "NumberOfThreads": 1,
  "WelcomeMessage": ""
}
EOL
fi
