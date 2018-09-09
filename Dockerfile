FROM ubuntu:14.04
MAINTAINER Germán Robledo <germix@germix.net>

ENV DEBIAN_FRONTEND=noninteractive

ENV AC_FOLDER=assetto

ENV STEAM_USER=
ENV STEAM_PASSWORD=

ENV AC_SERVER_NAME=AC_Server
ENV AC_PASSWORD=
ENV AC_ADMIN_PASSWORD=mypassword
ENV AC_UDP_PORT=9600
ENV AC_TCP_PORT=9600
ENV AC_HTTP_PORT=8081
ENV AC_PLUGIN_ADDRESS_LOCAL_PORT=10001
ENV AC_PLUGIN_LOCAL_PORT=10002

ENV ST_USERNAME=
ENV ST_PASSWORD=
ENV ST_HTTP_PORT=50041
ENV ST_PTRACKER_PORT=50042
ENV ST_SERVER_NAME=acserver

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y libc6:i386 libgcc1:i386 libstdc++6:i386 libz1:i386 libssl-dev:i386 libssl-dev lib32gcc1 unzip ca-certificates && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN [ "/bin/bash", "-c", "mkdir -p /opt/{assetto,steamcmd,stracker}" ]

COPY files/steamcmd_linux.tar.gz /opt/steamcmd/steamcmd.tar.gz
COPY files/stracker-V3.5.1.zip /opt/stracker/stracker.zip

ADD scripts/ /usr/local/bin

RUN unpack-all.sh

ENTRYPOINT [ "docker-entrypoint.sh" ]
