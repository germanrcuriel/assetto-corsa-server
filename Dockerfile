FROM germanrcuriel/steamcmd:latest
MAINTAINER Germán Robledo <germix@germix.net>

ENV STEAM_APP_ID 302550
ENV STEAM_APP_NAME assetto

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y libc6:i386 libgcc1:i386 libstdc++6:i386 libz1:i386 && \
    apt-get install -y curl unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /opt/stracker && \
    cd /opt/stracker && \
    curl http://www.n-e-y-s.de/downloads/stracker/stable/stracker-V3.4.1.zip --output stracker.zip && \
    unzip stracker.zip && \
    tar xvzf stracker_linux_x86.tgz && \
    rm stracker_linux_x86.tgz && \
    rm stracker.zip

ADD docker-entrypoint.sh /usr/local/bin

RUN apt-get remove -y curl unzip && \
    apt-get autoremove -y

EXPOSE 8081 9600 9600/udp 50041 50042

ENTRYPOINT [ "docker-entrypoint.sh" ]
