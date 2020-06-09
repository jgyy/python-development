"""
$Env:FLASK_ENV = "development"
$Env:FLASK_APP = './web_dev/notes'
flask run --host=0.0.0.0 --port=3000
"""
import os

from flask import Flask
from flask_migrate import Migrate

# Registering our Database with Our Application
def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from .models import db

    db.init_app(app)
    Migrate(app, db)

    return app