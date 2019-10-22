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
  sed -i "
    s/NAME=AC_Server.*$/NAME=${AC_SERVER_NAME}/
    s/PASSWORD=.*/PASSWORD=${AC_PASSWORD}/
    s/ADMIN_PASSWORD=mypassword.*/ADMIN_PASSWORD=${AC_ADMIN_PASSWORD}/
    s/UDP_PORT=9600.*/UDP_PORT=${AC_UDP_PORT}/
    s/TCP_PORT=9600.*/TCP_PORT=${AC_TCP_PORT}/
    s/HTTP_PORT=8081.*/HTTP_PORT=${AC_HTTP_PORT}/
    s/UDP_PLUGIN_LOCAL_PORT=0.*/UDP_PLUGIN_LOCAL_PORT=${AC_PLUGIN_LOCAL_PORT}/
    s/UDP_PLUGIN_ADDRESS=.*/UDP_PLUGIN_ADDRESS=127.0.0.1:${AC_PLUGIN_ADDRESS_LOCAL_PORT}/
  " cfg/server_cfg.ini
}

if [ ! -f $INSTALL_PATH/acServer ];  then
  install_assetto "Installing"
  setup_assetto
fi

if [ -n "${AC_FORCE_UPDATE}" ]; then
  install_assetto "Updating"
fi
