#!/bin/sh
set -e

export ASSETTO=/steamapps/${STEAM_APP_NAME:=$STEAM_APP_ID}

if [ ! -d "/steamapps/${STEAM_APP_NAME:=$STEAM_APP_ID}" ] || [ -n "${FORCE_UPDATE}" ]; then
  echo ">>> Installing/Updating Assetto Corsa Dedicated Server..."
  /opt/steamcmd/steamcmd.sh \
    +@sSteamCmdForcePlatformType windows \
    +login ${STEAM_USER:=anonymous} ${STEAM_PASSWORD} \
    +force_install_dir ${ASSETTO} \
    +app_update ${STEAM_APP_ID} \
    +quit
fi

if [ ! -d ${ASSETTO}/plugins/stracker ]; then
  cp -rf /opt/stracker ${ASSETTO}/plugins/stracker
fi

cd ${ASSETTO}/plugins/stracker

if [ ! -f stracker.ini ]; then
  cp stracker-default.ini stracker.ini
  sed -i '/ac_server_cfg_ini =/c\ac_server_cfg_ini = \.\./\.\./cfg/server_cfg.ini' stracker.ini
  sed -i '/enabled = False/c\enabled = True' stracker.ini
fi

echo ">>> Starting stracker..."
nohup ./stracker_linux_x86/stracker --stracker_ini stracker.ini &>/dev/null &

echo ">>> Starting Assetto Corsa Dedicated Server..."
cd ${ASSETTO}
./acServer
