# Docktical

## Getting started

Docktical is designed to create practical exercises in controlled environments by using Docker.

## Requirements

Docktical reguires 
- Docker;
- Python3;
- Alacritty.

## Usage

### docktical start

The `docktical start` command will start the practical work. It will download the images, build them, start the containers and open the terminal for the practical work.

!! Warning !!

The usage of `docker start --rebuild` will rebuild the containers so it will remove all the data in them. It can be used if one of the container reaches an invalid state.

### docktical open

The `docktical open` command is used to open a terminal on a running container. 

### docktical stop

The `docktical stop` command is used to stop the container that were running for the practical work. This command do not destroy the container states.

## Settings

A docktical project is mainly composed on two files. A `docker-composek.yml` file that contains the Docker compose configuration and a `docktical.yml` file that contains the docktical informations.

### Docktical settings

The docktical settings are really simple.

The user can specify one `tutorial` file which specify the path to the tutorial document and `terminals` which specifies the terminals list to be open.

A terminal can be specified with:
- `title`: The terminal title (optionnal, by default the title is set with the name of the container);
- `container`: The name of the container to run on;
- `script`: The program to execute (optional, by default the terminal will open a bash command).

The script argument should always link to a bash file.