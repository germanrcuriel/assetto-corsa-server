#!/bin/sh

if [ -f /opt/steamcmd/steamcmd.tar.gz ]; then
  echo ">>> Installing steamcmd"
  cd /opt/steamcmd
  tar xzf steamcmd.tar.gz
  rm steamcmd.tar.gz
fi

if [ -f /opt/minorating/minorating.zip ]; then
  echo ">>> Installing minorating"
  cd /opt/minorating
  unzip -qq minorating.zip
  rm minorating.zip
fi

if [ -f /opt/stracker/stracker.zip ]; then
  echo ">>> Installing stracker"
  cd /opt/stracker
  unzip -qq stracker.zip
  tar xzf stracker_linux_x86.tgz
  rm stracker.zip stracker_linux_x86.tgz
fi

if [ -f /opt/track-cycle/track-cycle.zip ]; then
  echo ">>> Installing track-cycle"
  cd /opt/track-cycle
  unzip -qq track-cycle.zip
  rm track-cycle.zip
fi
