#!/usr/bin/env sh

#Install necessary python packages
sudo apt install python3-pip python3-dev python3-setuptools python3-numpy python3-opencv libopencv-dev cmake libinih-dev

#Install missing howdy deb files
wget https://github.com/dingobits/howdy/releases/download/3.0.0-git20230625.c17a834/howdy_3.0.0.git20230625.c17a834-1_amd64_deb12.deb && wget https://github.com/dingobits/howdy/releases/download/3.0.0-git20230625.c17a834/python3-dlib_19.24.2-1_amd64_deb12.deb

#Install howdy deb files
sudo dpkg -i *.deb


cd /etc/howdy/dlib-data


sudo ./install.sh
