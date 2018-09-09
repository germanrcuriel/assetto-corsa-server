## assetto-corsa-server
[![](https://images.microbadger.com/badges/image/germanrcuriel/assetto-corsa-server.svg)](http://microbadger.com/images/germanrcuriel/assetto-corsa-server "Get your own image badge on microbadger.com") [![](https://images.microbadger.com/badges/version/germanrcuriel/assetto-corsa-server.svg)](http://microbadger.com/images/germanrcuriel/assetto-corsa-server "Get your own version badge on microbadger.com")

[Assetto Corsa Dedicated Server](https://steamdb.info/app/302550/) docker container.

### Usage
    docker run -d \
        --name assetto-corsa-server \
        -e PUID=<UID> -e PGID=<GID> \
        -e TZ=<timezone> \
        -e STEAM_USER=<Steam username> \
        -e STEAM_PASSWORD=<Steam password> \
        -p 8081:8081 \
        -p 9600:9600 \
        -p 9600:9600/udp \
        -p 50041:50041 \
        -p 50042:50042 \
        -v </path/to/install_dir>:/steamapps \
        germanrcuriel/assetto-corsa-server

This will install, config (for the first time only) and run:
- [Assetto Corsa Dedicated Server](https://steamdb.info/app/302550/)
- [stracker](http://www.n-e-y-s.de/main)

For a list of complete parameters, see below.

### Parameters

* `-e PUID` for UserID - see below for explanation.
* `-e PGID` for GroupID - see below for explanation.
* `-e TZ` for timezone information, for example, `Europe/Madrid`.
* `-e STEAM_USER` for your Steam account username. **Mandatory**.
* `-e STEAM_PASSWORD` for your Steam account password. **Mandatory**.

* `-p 8081:8081` Default Assetto Corsa HTTP port. **Mandatory**. Change it if `AC_HTTP_PORT` is different.
* `-p 9600:9600` Default Assetto Corsa TCP port. **Mandatory**. Change it if `AC_TCP_PORT` is different.
* `-p 9600:9600/udp` Default Assetto Corsa UDP port. **Mandatory**. Change it if `AC_UDP_PORT` is different.
* `-p 50041:50041` Default stracker HTTP port. **Mandatory**. Change it if `ST_HTTP_PORT` is different.
* `-p 50042:50042` Default ptracker port. **Mandatory**. Change it if `ST_PTRACKER_PORT` is different.

* `-v </path/to/install_dir>:/steamapps` - Base install path. **Mandatory**. A folder called `assetto` (or the one specified in `ASSETTO_FOLDER`) will be created under this volume.

#### Assetto Corsa Dedicated Server

* `-e AC_FOLDER` for the folder name you want to create for the installation. Defaults to `assetto`.
* `-e AC_FORCE_UPDATE` if set, it will force update Assetto Corsa Dedicated Server.
* `-e AC_SERVER_NAME` for the public server name. Defaults to `AC_Server`.
* `-e AC_PASSWORD` for setting a password to join the server.
* `-e AC_ADMIN_PASSWORD` for setting the admin password to handle the server.
* `-e AC_UDP_PORT`. Defaults to `9600`.
* `-e AC_TCP_PORT`. Defaults to `9600`.
* `-e AC_HTTP_PORT`. Defaults to `8081`.
* `-e AC_PLUGIN_LOCAL_PORT`. Defaults to `10001`.
* `-e AC_PLUGIN_ADDRESS_LOCAL_PORT`. Defaults to `10002`.


#### stracker

* `-e ST_USERNAME` to set password for the stracker admin pages.
* `-e ST_PASSWORD` to set the username for the stracker admin pages.
* `-e ST_HTTP_PORT` to change the port of stracker. Defaults to `50041`.
* `-e ST_SERVER_NAME` for tagging sessions in stracker. Defaults to `acserver`.

### User / Group identifiers

Sometimes when using data volumes (`-v` flags) permissions issues can arise between the host OS and the container. We avoid this issue by allowing you to specify the user `PUID` and group `PGID`. Ensure the data volume directory on the host is owned by the same user you specify and it will "just work" <sup>TM</sup>.

In this instance `PUID=1001` and `PGID=1001`. To find yours use `id user` as below:

```
  $ id <dockeruser>
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```
