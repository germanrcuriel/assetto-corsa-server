#!/bin/sh

export INSTALL_PATH="/steamapps/${ASSETTO_FOLDER}"

install-all.sh

cd $INSTALL_PATH
./acServer
