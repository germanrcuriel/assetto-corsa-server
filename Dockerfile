FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Madrid

ENV AC_FOLDER=assetto
ENV SHARED_FOLDER=shared

ENV STEAM_USER=
ENV STEAM_PASSWORD=

ENV AC_SERVER_NAME=AC_Server
ENV AC_PASSWORD=
ENV AC_ADMIN_PASSWORD=mypassword
ENV AC_UDP_PORT=9600
ENV AC_TCP_PORT=9600
ENV AC_HTTP_PORT=8081
ENV AC_PLUGIN_LOCAL_PORT=11001
ENV AC_PLUGIN_ADDRESS_LOCAL_PORT=12001

ENV UW_LOCAL_PORT=11001
ENV UW_PLUGIN_PORT=12001
ENV UW_PROXY_LOCAL_PORT=11002
ENV UW_PROXY_PLUGIN_PORT=12002
ENV UW_REDIS_ENABLED=true
ENV UW_REDIS_HOST=0.0.0.0
ENV UW_REDIS_PORT=6379
ENV UW_REDIS_PASSWORD=mypassword
ENV UW_REDIS_PUBLISH_CHANNEL=udp2ws.events
ENV UW_REDIS_SUBSCRIBE_CHANNEL=udp2ws.commands.*
ENV UW_PASSWORD=mypassword
ENV UW_PORT=30000

ENV SM_HTTP_PORT=9000

RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests lib32stdc++6 lib32gcc1 ca-certificates tzdata unzip wget \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN [ "/bin/bash", "-c", "mkdir -p /opt/{assetto,steamcmd,server-manager,udp2ws}" ]

COPY files/steamcmd_linux.tar.gz /opt/steamcmd/steamcmd.tar.gz
COPY files/server-manager_v1.7.4.zip /opt/server-manager/server-manager.zip
COPY files/udp2ws-v0.5.0.zip /opt/udp2ws/udp2ws.zip

ADD scripts/ /usr/local/bin

RUN unpack-all.sh

ENTRYPOINT [ "docker-entrypoint.sh" ]
