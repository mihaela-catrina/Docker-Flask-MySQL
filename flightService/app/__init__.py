from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask import jsonify
import requests

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello I am the service running here! DB is with me'

    @app.route('/book_flight', methods=['GET'])
    def book_flight():
        return render_template('book_flight.html')

    @app.route('/get_paths', methods=['GET'])
    def get_paths():
        path = []
        paths = []
        paths = functions.findPaths("a", "d", 3, 2, paths, path)
        return jsonify(paths=paths), 200

    @app.route('/book_flight', methods=['POST'])
    def book_flight_post():
        flight_id = request.form['flight_id']
        response = functions.book_flight(flight_id)

        if response == 1:
            return jsonify(response="Booking Succeeded!"), 200
        else:
            return jsonify(response="This flight is overbooked!"), 400

    login_manager.init_app(app)
    login_manager.login_message = 'You must be logged in to access this page'
    login_manager.login_view = 'auth.login'

    migrate = Migrate(app,db)

    from app import models
    from app import functions

    return app
