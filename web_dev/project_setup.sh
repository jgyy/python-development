#!/bin/sh

# The Basic Directory Structure
cd ~/projects
mkdir notes
cd notes
pipenv --python python3.7 install flask
pipenv shell
mkdir templates static
touch {templates,static}/.gitkeep

curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore
git init
$ git add --all .
$ git commit -m 'Initial commit'
