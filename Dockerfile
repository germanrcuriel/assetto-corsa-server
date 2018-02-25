FROM germanrcuriel/steamcmd:latest
MAINTAINER Germán Robledo <germix@germix.net>

ADD ./docker-entrypoint.sh /usr/local/bin

ENTRYPOINT [ "docker-entrypoint.sh" ]
