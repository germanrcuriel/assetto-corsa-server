## assetto-corsa-server
[![](https://images.microbadger.com/badges/image/germanrcuriel/assetto-corsa-server.svg)](http://microbadger.com/images/germanrcuriel/assetto-corsa-server "Get your own image badge on microbadger.com") [![](https://images.microbadger.com/badges/version/germanrcuriel/assetto-corsa-server.svg)](http://microbadger.com/images/germanrcuriel/assetto-corsa-server "Get your own version badge on microbadger.com")

An [Assetto Corsa Dedicated Server](https://steamdb.info/app/302550/) docker container.

### Usage
    docker create \
        --name assetto-corsa-server \
        -e PUID=<UID> -e PGID=<GID> \
        -e TZ=<timezone> \
        -e STEAM_USER=<Steam username> \
        -e STEAM_PASSWORD=<Steam password> \
        -e STEAM_APP_NAME=<Steam Application Folder Name> \
        -p 8081:8081 \
        -p 9600:9600 \
        -p 9600:9600/udp \
        -v </path/to/install_dir>:/steamapps \
        germanrcuriel/assetto-corsa-server

### Parameters

* `-e PUID` for UserID - see below for explanation.
* `-e PGID` for GroupID - see below for explanation.
* `-e TZ` for timezone information, Europe/Madrid.
* `-e STEAM_USER` for your Steam account username. **Mandatory**.
* `-e STEAM_PASSWORD` for your Steam account password. **Mandatory**.
* `-e STEAM_APP_NAME` for the folder name you want to create for the installation.
* `-p 8081:8081` Default Assetto Corsa HTTP port.
* `-p 9600:9600` Default Assetto Corsa TCP port.
* `-p 9600:9600/udp` Default Assetto Corsa UDP port.
* `-v </path/to/install_dir>:/steamapps` - Assetto Corsa Dedicated Server base install path. A folder called `assetto` will be created under this volume unless `STEAM_APP_NAME` has been defined.

### TODO

* Add support for windows installations.
* Add `server_cfg.ini` template and the ability to config everything with ENV variables.

### User / Group identifiers

Sometimes when using data volumes (`-v` flags) permissions issues can arise between the host OS and the container. We avoid this issue by allowing you to specify the user `PUID` and group `PGID`. Ensure the data volume directory on the host is owned by the same user you specify and it will "just work" <sup>TM</sup>.

In this instance `PUID=1001` and `PGID=1001`. To find yours use `id user` as below:

```
  $ id <dockeruser>
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```
