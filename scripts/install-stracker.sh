#!/bin/sh

STRACKER_PATH="$INSTALL_PATH/plugins/stracker"

cd /opt/stracker

if [ ! -d $STRACKER_PATH ]; then
  cp stracker-default.ini stracker.ini
  sed -i "
    s/ac_server_cfg_ini =.*/ac_server_cfg_ini = \.\.\/\.\.\/cfg\/server_cfg.ini/
    s/admin_password =.*/admin_password = ${ST_PASSWORD}/
    s/admin_username =.*/admin_username = ${ST_USERNAME}/
    s/enabled = False.*/enabled = True/
    s/listen_port =.*/listen_port = ${ST_HTTP_PORT}/
    s/log_timestamps = False.*/log_timestamps = True/
    s/server_name = acserver.*/server_name = ${ST_SERVER_NAME}/
    s/items_per_page = 15.*/items_per_page = 20/
  " stracker.ini
  cp -rf . $STRACKER_PATH
fi
