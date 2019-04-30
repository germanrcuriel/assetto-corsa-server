#!/bin/sh

TRACK_CYCLE_PATH="$INSTALL_PATH/plugins/track-cycle"

cd /opt/track-cycle

if [ ! -d $TRACK_CYCLE_PATH ]; then
  cp AC_TrackCycle_Console.exe.config AC_TrackCycle_Console.exe.config_DEFAULT
  sed -i "
    s#<add key=\"ac_server_directory\" value=\"\"/>#<add key=\"ac_server_directory\" value=\"../../\"/>#
    s#<add key=\"welcome_message\".*#<add key=\"welcome_message\" value=\"${TC_WELCOME_MESSAGE}\" />#
    s#<!--<add key=\"external_plugins\".*#<add key=\"external_plugins\" value=\"Server Manager, ${TC_PROXY_LOCAL_PORT}, 127.0.0.1:${TC_PROXY_PLUGIN_PORT}\" />#
    /<appSettings>/a \    <add key=\"plugin_port\" value=\"${TC_PLUGIN_PORT}\" \/>
    /<appSettings>/a \    <add key=\"ac_server_port\" value=\"${TC_LOCAL_PORT}\" \/>
  " AC_TrackCycle_Console.exe.config
  cp -rf . $TRACK_CYCLE_PATH
fi
