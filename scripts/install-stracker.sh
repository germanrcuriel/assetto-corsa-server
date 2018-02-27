#!/bin/sh

STRACKER_PATH="$INSTALL_PATH/plugins/stracker"

cd /opt/stracker

if [ ! -f $STRACKER_PATH ]; then
  cp stracker-default.ini stracker.ini
  sed -i "s/ac_server_cfg_ini =.*/ac_server_cfg_ini = \.\.\/\.\.\/cfg\/server_cfg.ini/
          s/admin_password =.*/admin_password = ${STRACKER_PASSWORD}/
          s/admin_username =.*/admin_username = ${STRACKER_USERNAME}/
          s/enabled = False.*/enabled = True/
          s/listen_port =.*/listen_port = ${STRACKER_HTTP_PORT}/
          s/log_timestamps = False.*/log_timestamps = True/
          s/server_name = acserver.*/server_name = ${STRACKER_SERVER_NAME}/
          s/items_per_page = 15.*/items_per_page = 20/
          s/proxyPluginLocalPort = -1.*/proxyPluginLocalPort = ${STRACKER_PROXY_PLUGIN_LOCAL_PORT}/
          s/proxyPluginPort = -1.*/proxyPluginPort = ${STRACKER_PROXY_PLUGIN_PORT}/" stracker.ini
  cp -rf . $STRACKER_PATH
fi

cd $STRACKER_PATH

nohup ./stracker_linux_x86/stracker --stracker_ini stracker.ini >/dev/null 2>&1 &
