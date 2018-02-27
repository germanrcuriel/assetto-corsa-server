#!/bin/sh

TRACK_CYCLE_PATH="$INSTALL_PATH/plugins/track-cycle"

cd /opt/track-cycle

if [ ! -f $TRACK_CYCLE_PATH ]; then
  cp -rf . $TRACK_CYCLE_PATH
fi
