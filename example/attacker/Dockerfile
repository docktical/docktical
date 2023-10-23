FROM ubuntu:jammy

# Installing required packages
RUN apt update \
  && apt install -y \
    python3 nano net-tools iputils-ping curl

# Defining default non-root user UID, GID, and name
ARG USER_UID="1000"
ARG USER_GID="1000"
ARG USER_NAME="user"

# Creating default non-user
RUN groupadd -g $USER_GID $USER_NAME\
    && useradd -m -g $USER_GID -u $USER_UID $USER_NAME

# Change to non-root user
USER user
WORKDIR /home/user

SHELL [ "/bin/bash", "-c" ]
ENTRYPOINT [ "sleep", "infinity" ]