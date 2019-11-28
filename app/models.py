from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

class Flight(db.Model):
    """
    Create an Flight table
    """
    __tablename__ = 'flights'
    __table_args__ = (
        db.CheckConstraint('departure_hour > -1'),
        db.CheckConstraint('departure_hour < 24'),
    )
    id = db.Column(db.String(255), primary_key=True)
    source = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    departure_hour = db.Column(db.Integer)
    departure_day = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    seats = db.Column(db.Integer)


class Employee(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)


class Department(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)