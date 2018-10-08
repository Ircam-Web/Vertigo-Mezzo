FROM ircamweb/mezzo:latest-dev

WORKDIR /srv

COPY lib /srv/lib
RUN bash setup_lib.sh

WORKDIR /srv/app
