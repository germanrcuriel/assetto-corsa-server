#!/bin/sh

ulimit -n 90000

export INSTALL_PATH="/steamapps/${AC_FOLDER}"

install-all.sh

cd $INSTALL_PATH/plugins/stracker/stracker_linux_x86
./stracker --stracker_ini stracker.ini