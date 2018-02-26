#!/bin/sh

echo ">>> Updating Assetto Corsa Dedicated Server..."
install-steam-app.sh

echo ">>> Starting Assetto Corsa Dedicated Server..."
cd /steamapps/${STEAM_APP_NAME:=$STEAM_APP_ID}
./acServer
