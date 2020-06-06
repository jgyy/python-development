#!/bin/sh

# Creating Our First Python Script
echo 'print("Hello, World!")' > hello.py
chmod u+x hello.py
python3 hello.py

# Adding Scripts to Our $PATH
mkdir ~/bin
mv hello.py ~/bin/hello
export PATH=$PATH:$HOME/bin
hello
