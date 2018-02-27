#!/bin/sh
set -e

cd /opt/steamcmd

install_assetto() {
  echo ">>> $1 Assetto Corsa Dedicated Server"
  ./steamcmd.sh \
    +@sSteamCmdForcePlatformType windows \
    +login ${STEAM_USER:=anonymous} ${STEAM_PASSWORD} \
    +force_install_dir $INSTALL_PATH \
    +app_update 302550 \
    +quit
}

setup_assetto() {
  echo ">>> Setting up Assetto Corsa Dedicated Server"
  cd $INSTALL_PATH
  mkdir -p plugins
  sed -i "s/NAME=AC_Server.*$/NAME=${AC_SERVER_NAME}/
          s/PASSWORD=.*/PASSWORD=${AC_SERVER_PASSWORD}/
          s/ADMIN_PASSWORD=mypassword.*/ADMIN_PASSWORD=${AC_SERVER_ADMIN_PASSWORD}/
          s/UDP_PORT=9600.*/UDP_PORT=${AC_SERVER_UDP_PORT}/
          s/TCP_PORT=9600.*/TCP_PORT=${AC_SERVER_TCP_PORT}/
          s/HTTP_PORT=8081.*/HTTP_PORT=${AC_SERVER_HTTP_PORT}/
          s/UDP_PLUGIN_LOCAL_PORT=0.*/UDP_PLUGIN_LOCAL_PORT=${AC_PLUGIN_LOCAL_PORT}/
          s/UDP_PLUGIN_ADDRESS=.*/UDP_PLUGIN_ADDRESS=127.0.0.1:${AC_PLUGIN_ADDRESS_LOCAL_PORT}/
          s/AUTH_PLUGIN_ADDRESS=.*/AUTH_PLUGIN_ADDRESS=${AC_AUTH_PLUGIN_ADDRESS}/" cfg/server_cfg.ini
}

if [ ! -d $INSTALL_PATH ];  then
  install_assetto "Installing"
  setup_assetto
fi

if [ -n "${ASSETTO_FORCE_UPDATE}" ]; then
  install_assetto "Updating"
fi
