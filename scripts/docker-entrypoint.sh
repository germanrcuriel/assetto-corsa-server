#!/bin/sh

ulimit -n 90000

export INSTALL_PATH="/steamapps/${AC_FOLDER}"

install-all.sh

cd $INSTALL_PATH/plugins/udp2ws
nohup ./udp2ws >/dev/null 2>&1 &

cd $INSTALL_PATH/plugins/track-cycle
mono ./AC_TrackCycle_Console.exe