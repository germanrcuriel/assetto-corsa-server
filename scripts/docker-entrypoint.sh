#!/bin/sh

export INSTALL_PATH="/steamapps/${AC_FOLDER}"

install-all.sh

cd $INSTALL_PATH/plugins/stracker
nohup ./stracker_linux_x86/stracker --stracker_ini stracker.ini >/dev/null 2>&1 &

cd $INSTALL_PATH
./acServer
