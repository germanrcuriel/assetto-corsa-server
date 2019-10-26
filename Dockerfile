FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Madrid

ENV AC_FOLDER=assetto

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

ENV ST_SERVER_NAME=AC_Server
ENV ST_PORT=50042
ENV ST_POSTGRES_DB=stracker
ENV ST_POSTGRES_HOST=localhost
ENV ST_POSTGRES_USER=myuser
ENV ST_POSTGRES_PASSWORD=password
ENV ST_USERNAME=
ENV ST_PASSWORD=
ENV ST_HTTP_ENABLED=True
ENV ST_HTTP_PORT=50041
ENV ST_WELCOME_MSG_LINE1=
ENV ST_WELCOME_MSG_LINE2=
ENV ST_WELCOME_MSG_LINE3=
ENV ST_WELCOME_MSG_LINE4=
ENV ST_WELCOME_MSG_LINE5=
ENV ST_WELCOME_MSG_LINE6=
ENV ST_PROXY_PLUGIN_LOCAL_PORT=-1
ENV ST_PROXY_PLUGIN_PORT=-1
ENV ST_RCV_PORT=12002
ENV ST_SEND_PORT=11002

ENV UW_LOCAL_PORT=11001
ENV UW_PLUGIN_PORT=12001
ENV UW_PROXY_LOCAL_PORT=11002
ENV UW_PROXY_PLUGIN_PORT=12002
ENV UW_PASSWORD=mypassword
ENV UW_PORT=30000

ENV SM_HTTP_PORT=9000

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y libc6:i386 libgcc1:i386 libstdc++6:i386 libz1:i386 libssl-dev:i386 libssl-dev lib32gcc1 unzip ca-certificates tzdata && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN [ "/bin/bash", "-c", "mkdir -p /opt/{assetto,steamcmd,server-manager,stracker,udp2ws}" ]

COPY files/steamcmd_linux.tar.gz /opt/steamcmd/steamcmd.tar.gz
COPY files/server-manager_v1.5.2.zip /opt/server-manager/server-manager.zip
COPY files/stracker-V3.5.3.zip /opt/stracker/stracker.zip
COPY files/udp2ws-v0.3.1.zip /opt/udp2ws/udp2ws.zip

ADD scripts/ /usr/local/bin

RUN unpack-all.sh

ENTRYPOINT [ "docker-entrypoint.sh" ]
