#!/bin/sh

if [ -f /opt/steamcmd/steamcmd.tar.gz ]; then
  echo ">>> Installing steamcmd"
  cd /opt/steamcmd
  tar xzf steamcmd.tar.gz
  rm steamcmd.tar.gz
fi

if [ -f /opt/server-manager/server-manager.zip ]; then
  echo ">>> Installing server-manager"
  cd /opt/server-manager
  unzip -qq server-manager.zip
  rm server-manager.zip
fi

if [ -f /opt/udp2ws/udp2ws.zip ]; then
  echo ">>> Installing udp2ws"
  cd /opt/udp2ws
  unzip -qq udp2ws.zip
  rm udp2ws.zip
fi

if [ -f /opt/track-cycle/track-cycle.zip ]; then
  echo ">>> Installing track-cycle"
  cd /opt/track-cycle
  unzip -qq track-cycle.zip
  rm track-cycle.zip
fi
