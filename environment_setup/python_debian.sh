#!/bin/sh

# Download and Install Python 3 from Source
apt update -y
apt install -y wget build-essential libffi-dev libgdbm-dev \
libc6-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
libsqlite3-dev libncurses5-dev libncursesw5-dev xz-utils tk-dev
cd /usr/src
wget http://python.org/ftp/python/3.8.2/Python-3.8.2.tar.xz
tar xf Python-3.8.2.tar.xz
cd Python-3.8.2
./configure --enable-optimizations
make altinstall

# Upgrade Pip
pip3.8 install --upgrade pip
