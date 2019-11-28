from app import models

def add_flight(source, destination, departureDay, departureHour, duration, seats, id):
    flight = models.Flight(id=id, source=source, destination=destination, duration=duration, seats=seats, departure_hour=departureHour, departure_day=departureDay)
    models.db.session.add(flight)
    models.db.session.commit()
    return 'Make something!'

