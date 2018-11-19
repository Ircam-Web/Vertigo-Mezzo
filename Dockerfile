FROM ircamweb/mezzo:latest

WORKDIR /srv

COPY lib /srv/lib
RUN bash setup_lib.sh

WORKDIR /srv/app
