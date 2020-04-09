#!/bin/sh

ulimit -n 90000

export INSTALL_PATH="/steamapps/${AC_FOLDER}"

if [ -n ${SHARED_FOLDER+x} ]; then
    export SHARED_PATH="/steamapps/${SHARED_FOLDER}"
fi

install-all.sh

cd $INSTALL_PATH/plugins/udp2ws
nohup ./udp2ws >/dev/null 2>&1 &

cd $INSTALL_PATH/plugins/server-manager
./server-manager