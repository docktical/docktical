FROM ubuntu:jammy

# Installing required packages
RUN apt update \
  && apt install -y \
    python3 nano net-tools iputils-ping screen

# Defining default non-root user UID, GID, and name
ARG USER_UID="1000"
ARG USER_GID="1000"
ARG USER_NAME="user"

# Creating default non-user
RUN groupadd -g $USER_GID $USER_NAME\
    && useradd -m -g $USER_GID -u $USER_UID $USER_NAME

# Install logging script
WORKDIR /opt
COPY logs.sh logs.sh
RUN chmod u=rx,g=rx,o=rx logs.sh
RUN touch .logs && chmod o+w .logs

# Change to non-root user
USER user

# Install webserver
WORKDIR /home/user
COPY init.sh init.sh

SHELL [ "/bin/bash", "-c" ]
ENTRYPOINT [ "/bin/bash", "init.sh" ]