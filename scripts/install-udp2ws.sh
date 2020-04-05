#!/bin/sh

UDP2WS_PATH="$INSTALL_PATH/plugins/udp2ws"

cd /opt/udp2ws/linux_x64

if [ ! -d $UDP2WS_PATH ]; then
  sed -i "
    s/proxyPluginLocalPort =.*/proxyPluginLocalPort = ${UW_PROXY_LOCAL_PORT}/
    s/proxyPluginPort =.*/proxyPluginPort = ${UW_PROXY_PLUGIN_PORT}/
    s/sendPort =.*/sendPort = ${UW_LOCAL_PORT}/
    s/receivePort =.*/receivePort = ${UW_PLUGIN_PORT}/
    s/enabled =.*/enabled = ${UW_REDIS_ENABLED}/
    s/host =.*/host = ${UW_REDIS_HOST}/
    s/port =.*/port = ${UW_REDIS_PORT}/
    s/password =.*/password = ${UW_REDIS_PASSWORD}/

    s/; password =.*/password = ${UW_PASSWORD}/
    s/port =.*/port = ${UW_PORT}/
  " udp2ws.ini
  cp -rf . $UDP2WS_PATH
fi
