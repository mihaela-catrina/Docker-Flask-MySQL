from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://db_admin:db_admin@db/sprc_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello World ! I am back with db running .!'

    migrate = Migrate(app,db)

    from app import models

    return app
