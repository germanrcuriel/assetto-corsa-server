#!/bin/sh

if [ -f /opt/steamcmd/steamcmd.tar.gz ]; then
  echo ">>> Installing steamcmd"
  cd /opt/steamcmd
  tar xzf steamcmd.tar.gz
  rm steamcmd.tar.gz
fi

if [ -f /opt/stracker/stracker.zip ]; then
  echo ">>> Installing stracker"
  cd /opt/stracker
  unzip -qq stracker.zip
  tar xzf stracker_linux_x86.tgz
  rm stracker.zip stracker_linux_x86.tgz
fi
