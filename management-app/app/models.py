from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

class Flight(db.Model):
    """
    Create an Flight table
    """
    __tablename__ = 'flights'

    id = db.Column(db.String(255), primary_key=True)
    source = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    departure_hour = db.Column(db.Integer)
    departure_day = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    seats = db.Column(db.Integer)

    __table_args__ = (
        db.CheckConstraint(db.and_(departure_hour >= 0, departure_hour <= 23)),
        db.CheckConstraint(db.and_(departure_day >= 1, departure_day <= 365)),
    )

class Booking(db.Model):
    """
    Create an Flight table
    """
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    flight_ids = db.Column(db.String(255), nullable=False)


class Ticket(db.Model):
    """
    Create a table for the tickets already bought
    """
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer)
