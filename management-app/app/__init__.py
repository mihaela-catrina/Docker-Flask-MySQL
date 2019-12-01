from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask import jsonify

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello World ! I am back with db running .!'

    @app.route('/add_flight', methods=['GET'])
    def add_flight():
        return render_template('add_flight.html')

    @app.route('/add_flight', methods=['POST'])
    def add_flight_post():
        source = request.form['source']
        destination = request.form['destination']
        departureDay = request.form['departureDay']
        departureHour = request.form['departureHour']
        duration = request.form['duration']
        seats = request.form['seats']
        id = request.form['id']
        res = functions.add_flight(source, destination, departureDay, departureHour, duration, seats, id)
        if res:
            return jsonify(response="Flight added!"), 200
        else:
            return jsonify(response="Try another ID -> this flight exists!"), 200

    @app.route('/remove_flight', methods=['GET'])
    def remove_flight():
        return render_template('remove_flight.html')

    @app.route('/remove_flight', methods=['POST'])
    def remove_flight_post():
        id = request.form['id']
        rsp = functions.remove_flight(id)
        if rsp:
            return jsonify(response="Flight removed!"), 200
        else:
            return jsonify(response="We can't find this flight!"), 400

    login_manager.init_app(app)
    login_manager.login_message = 'You must be logged in to access this page'
    login_manager.login_view = 'auth.login'

    migrate = Migrate(app,db)

    from app import models
    from app import functions

    return app
