#!/bin/sh

# Installing Development tools and Vim
yum update -y
yum groupinstall -y "development tools"
yum install -y vim-enhanced

# Configure git
git config --global user.name "Keith Thompson"
git config --global user.email "keith@gmail.com"

# Pull down sample bashrc
curl https://raw.githubusercontent.com/linuxacademy/content-intro-to-python-development/master/helpers/bashrc -o ~/.bashrc
exec $SHELL

# Pull down sample vimrc
curl https://raw.githubusercontent.com/linuxacademy/content-intro-to-python-development/master/helpers/vimrc -o ~/.vimrc

# Demonstrat PS1 changes
mkdir sample
cd sample
touch file.txt
git init
git add --all .
git commit -m 'Initial commit'
