#!/usr/bin/env bash
# script to install python 3.7


# download python3.7
sudo cd /usr/src
sudo wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz

# unzip the tarball
sudo tar xf Python-3.7.3.tar.xz
cd Python-3.7.3.tar.xz

# run the configuration file
sudo ./configure --enable-optimizations --with-ensurepip=install
sudo make altinstall

# upgrade pip
sudo pip3.7 install --upgrade pip

# install requests library
sudo pip3 install requests