FROM ircamweb/mezzo:latest

WORKDIR /srv

COPY lib /srv/lib
COPY bin/build/local/setup_lib.sh /srv

RUN bash setup_lib.sh

WORKDIR /srv/app
