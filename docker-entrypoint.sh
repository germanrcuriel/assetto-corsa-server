#!/bin/sh

echo "Starting Assetto Corsa Server..."
cd /steamapps/${STEAM_APP_NAME:=$STEAM_APP_ID}
./acServer
