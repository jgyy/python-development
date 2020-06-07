#!/bin/sh

# Let's install our first package, the popular AWS client library boto3
pip install --user boto3
pip freeze > requirements.txt
pip install --user -r requirements.txt

# Creating a virtualenv
mkdir ~/venvs
python -m venv ~/venvs/pg
source ~/venvs/pg/bin/activate
pip install psycopg2
deactivate

# Using pipenv
pip install --user pipenv
mkdir ~/database
cd ~/database
pipenv --python python
pipenv shell
. /home/cloud_user/.local/share/virtualenvs/database-OGMn9Yao/bin/activate
pipenv install psycopg2
exit
