#!/bin/sh

MINORATING_PATH="$INSTALL_PATH/plugins/minorating"

cd /opt/minorating

if [ ! -f $MINORATING_PATH ]; then
  cp -rf . $MINORATING_PATH
fi
