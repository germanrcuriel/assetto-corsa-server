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

if [ -f /opt/stracker/stracker.zip ]; then
  echo ">>> Installing stracker"
  cd /opt/stracker
  unzip -qq stracker.zip
  tar xzf stracker_linux_x86.tgz
  rm stracker.zip stracker_linux_x86.tgz
fi

if [ -f /opt/udp2ws/udp2ws.zip ]; then
  echo ">>> Installing udp2ws"
  cd /opt/udp2ws
  unzip -qq udp2ws.zip
  rm udp2ws.zip
fi