from app import models

def add_flight(source, destination, departureDay, departureHour, duration, seats, id):
    try:
        flight = models.Flight(id=id, source=source, destination=destination, duration=duration, seats=seats, departure_hour=departureHour, departure_day=departureDay)
        models.db.session.add(flight)
        models.db.session.commit()
        return True
    except Exception as _:
        return False


def remove_flight(id):
    try:
        obj = models.Flight.query.filter_by(id=id).one()
        models.db.session.delete(obj)
        models.db.session.commit()
        return True
    except Exception as _:
        return False
