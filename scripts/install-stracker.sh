#!/bin/sh

STRACKER_PATH="$INSTALL_PATH/plugins/stracker"

cd /opt/stracker

if [ ! -d $STRACKER_PATH ]; then
  cp stracker-default.ini stracker_linux_x86/stracker.ini
  sed -i "
    s/ac_server_cfg_ini =.*/ac_server_cfg_ini = \.\.\/\.\.\/\.\.\/cfg\/server_cfg.ini/
    s/listening_port =.*/listening_port = ${ST_PORT}/
    s/log_timestamps = False.*/log_timestamps = True/
    s/server_name = acserver.*/server_name = ${ST_SERVER_NAME}/
    s/tee_to_stdout =.*/tee_to_stdout = True/
    s/database_type = sqlite3.*/database_type = postgres/
    s/postgres_db = stracker.*/postgres_db = ${ST_POSTGRES_DB}/
    s/postgres_host = localhost.*/postgres_host = ${ST_POSTGRES_HOST}/
    s/postgres_pwd = password.*/postgres_pwd = ${ST_POSTGRES_PASSWORD}/
    s/postgres_user = myuser.*/postgres_user = ${ST_POSTGRES_USER}/
    s/admin_password =.*/admin_password = ${ST_PASSWORD}/
    s/admin_username =.*/admin_username = ${ST_USERNAME}/
    s/enabled = False.*/enabled = ${ST_HTTP_ENABLED}/
    s/items_per_page = 15.*/items_per_page = 25/
    s/listen_port =.*/listen_port = ${ST_HTTP_PORT}/
    s/line1 =.*/line1 = ${ST_WELCOME_MSG_LINE1}/
    s/line2 =.*/line2 = ${ST_WELCOME_MSG_LINE2}/
    s/line3 =.*/line3 = ${ST_WELCOME_MSG_LINE3}/
    s/line4 =.*/line4 = ${ST_WELCOME_MSG_LINE4}/
    s/line5 =.*/line5 = ${ST_WELCOME_MSG_LINE5}/
    s/line6 =.*/line6 = ${ST_WELCOME_MSG_LINE6}/
    s/proxyPluginLocalPort =.*/proxyPluginLocalPort = ${ST_PROXY_PLUGIN_LOCAL_PORT}/
    s/proxyPluginPort =.*/proxyPluginPort = ${ST_PROXY_PLUGIN_PORT}/
    s/rcvPort =.*/rcvPort = ${ST_RCV_PORT}/
    s/sendPort =.*/sendPort = ${ST_SEND_PORT}/
  " stracker_linux_x86/stracker.ini
  cp -rf . $STRACKER_PATH
fi