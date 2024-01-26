#!/usr/bin/env sh


#https://github.com/boltgolt/howdy/issues/858
#Install necessary python packages
sudo apt install libdbus-1-dev python3-evdev python3-pydbus libgtksourceview-4-dev python3-pydantic
cd /etc/howdy/dlib-data
sudo ./install.sh
sudo dpkg -i ./*.deb
