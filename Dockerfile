FROM germanrcuriel/steamcmd:latest
MAINTAINER Germán Robledo <germix@germix.net>

ENV STEAM_APP_ID 302550
ENV STEAM_APP_NAME assetto

ADD ./docker-entrypoint.sh /usr/local/bin

ENTRYPOINT [ "docker-entrypoint.sh" ]
