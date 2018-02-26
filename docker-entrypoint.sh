#!/bin/sh
set -e

echo ">>> Updating Assetto Corsa Dedicated Server..."
/opt/steamcmd/steamcmd.sh \
  +@sSteamCmdForcePlatformType ${STEAM_PLATFORM:=linux} \
  +login ${STEAM_USER:=anonymous} ${STEAM_PASSWORD} \
  +force_install_dir /steamapps/${STEAM_APP_NAME:=$STEAM_APP_ID} \
  +app_update ${STEAM_APP_ID} \
  +quit

echo ">>> Starting Assetto Corsa Dedicated Server..."
cd /steamapps/${STEAM_APP_NAME:=$STEAM_APP_ID}
./acServer
