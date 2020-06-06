#!/bin/sh

# Download and Install Python 3 from Source
yum groupinstall -y "development tools"
yum install -y libffi-devel zlib-devel bzip2-devel openssl-devel \
ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel \ 
libpcap-devel xz-devel expat-devel postgresql-devel
cd /usr/src
wget http://python.org/ftp/python/3.8.2/Python-3.8.2.tar.xz
tar xf Python-3.8.2.tar.xz
cd Python-3.8.2
./configure --enable-optimizations
make altinstall

# Upgrade Pip
pip3.7 install --upgrade pip
