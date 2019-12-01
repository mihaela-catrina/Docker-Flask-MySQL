from flask import Flask
from flask import render_template, request
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

    @app.route('/book_flights', methods=['GET'])
    def book_flights():
        return render_template('book_flight.html')

    @app.route('/buy_ticket', methods=['GET'])
    def buy_ticket():
        return render_template('buy_ticket.html')

    @app.route('/get_optimal_path', methods=['GET'])
    def get_paths():
        return render_template("get_optimal_path.html")

    @app.route('/get_optimal_path', methods=['POST'])
    def get_paths_post():
        source = request.form["source"]
        dst = request.form["destination"]
        max_flights = int(request.form["max_flights"])
        dep_day = int(request.form["departure_day"])
        path = functions.get_optimal_route(source, dst, max_flights, dep_day)
        return jsonify(paths=path), 200

    @app.route('/book_flights', methods=['POST'])
    def book_flights_post():
        flight_ids = request.form['flight_ids']
        response = functions.book_flights(flight_ids)

        if response != 0:
            resp = "You booking id: " + str(response)
            return jsonify(response=resp), 200
        else:
            return jsonify(response="The flights are overbooked!"), 400

    @app.route('/buy_ticket', methods=['POST'])
    def buy_ticket_post():
        reservation_id = request.form['reservation_id']
        response = functions.buy_ticket(reservation_id)

        if response != 0:
            return jsonify(response="Congratulations, you have a ticket now!"), 200
        else:
            return jsonify(response="You need to make a reservation first"), 400

    login_manager.init_app(app)
    login_manager.login_message = 'You must be logged in to access this page'
    login_manager.login_view = 'auth.login'

    migrate = Migrate(app,db)

    from app import models
    from app import functions

    return app
