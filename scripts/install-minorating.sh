#!/bin/sh

MINORATING_PATH="$INSTALL_PATH/plugins/minorating"

cd /opt/minorating

if [ ! -d $MINORATING_PATH ]; then
  cp MinoRatingPlugin.exe.config_DEFAULT MinoRatingPlugin.exe.config
  sed -i "
    s#<!--<add key=\"ac_server_port\" value=\"11000\" />-->#<add key=\"ac_server_port\" value=\"${MR_LOCAL_PORT}\" />#
    s#<!--<add key=\"plugin_port\" value=\"12000\" />-->#<add key=\"plugin_port\" value=\"${MR_PLUGIN_PORT}\" />#
    s#<!--<add key=\"external_plugins\" value=\"OtherPluginName, 11001, 127.0.0.1:12001\"/>-->#<add key=\"external_plugins\" value=\"TrackCycle, ${MR_PROXY_LOCAL_PORT}, 127.0.0.1:${MR_PROXY_PLUGIN_PORT}\"/>#
  " MinoRatingPlugin.exe.config
  cp -rf . $MINORATING_PATH
fi
