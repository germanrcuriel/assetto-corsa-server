FROM mono:latest
MAINTAINER Germán Robledo <germix@germix.net>

ENV ASSETTO_FOLDER=assetto

ENV STEAM_USER=
ENV STEAM_PASSWORD=

ENV AC_SERVER_NAME=AC_Server
ENV AC_SERVER_PASSWORD=
ENV AC_SERVER_ADMIN_PASSWORD=mypassword
ENV AC_SERVER_UDP_PORT=9600
ENV AC_SERVER_TCP_PORT=9600
ENV AC_SERVER_HTTP_PORT=8081
ENV AC_PLUGIN_ADDRESS_LOCAL_PORT=10001
ENV AC_PLUGIN_LOCAL_PORT=10002
ENV AC_AUTH_PLUGIN_ADDRESS=

ENV STRACKER_USERNAME=
ENV STRACKER_PASSWORD=
ENV STRACKER_HTTP_PORT=50041
ENV STRACKER_SERVER_NAME=acserver
ENV STRACKER_PROXY_PLUGIN_PORT=11001
ENV STRACKER_PROXY_PLUGIN_LOCAL_PORT=11002

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y libc6:i386 libgcc1:i386 libstdc++6:i386 libz1:i386 lib32gcc1 unzip && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN [ "/bin/bash", "-c", "mkdir -p /opt/{assetto,steamcmd,stracker,minorating,track-cycle}" ]

ADD https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz /opt/steamcmd/steamcmd.tar.gz
ADD http://www.n-e-y-s.de/downloads/stracker/stable/stracker-V3.4.1.zip /opt/stracker/stracker.zip
ADD http://www.minorating.com/download/MinoRatingPlugin_2.4.2.zip /opt/minorating/minorating.zip
ADD https://github.com/flitzi/AC_SERVER_APPS/releases/download/v2.7.9/AC_TrackCycle_2.7.9.zip /opt/track-cycle/track-cycle.zip

ADD scripts/ /usr/local/bin

RUN unpack-all.sh

ENTRYPOINT [ "docker-entrypoint.sh" ]
