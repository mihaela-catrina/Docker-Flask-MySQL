from app import models
from app import graph


def verify_overbooking(flight_id, bookings):
    obj = models.db.session.query(models.Flight).filter_by(id=flight_id).one()
    seats = obj.seats
    overload = (seats * 11) / 10
    x = (bookings > overload)
    return x


def book_flight(flight_id):
    bookings = models.Booking.query.all()
    count = 0
    for book in bookings:
        if book.flight_id == flight_id:
            count = count + 1
    rsp = verify_overbooking(flight_id, count)
    if rsp is not True:
        booking = models.Booking(flight_id=flight_id)
        models.db.session.add(booking)
        models.db.session.commit()
        return 1
    else:
        return 0

# def verify_consistency(path, day, max_flights)

# source, flightID, duration, departure_day, destination
# def findPaths(s, d, day, max_flights, paths, path):
#
#     path.append(s)
#
#     if s == d:
#         paths.append({"path": list(path)})
#     else:
#         flights = models.db.session.query(models.Flight).filter_by(source=s).all()
#         for flight in flights:
#             path.append(flight.id)
#             path.append(flight.duration)
#             path.append(flight.departure_day)
#             findPaths(flight.destination, d, day, max_flights, paths, path)
#
#     path.pop()
#     if not path:
#         return paths
#
#     path.pop()
#     path.pop()
#     path.pop()
#     if not path:
#         return paths

# def verify_consistency(path, day, max_flights)


def findPaths(s, d, day, max_flights, paths, path):

    dict = {}
    dict["source"] = s
    path.append(dict)

    if s == d:
        if len(path) > 0:
            path.pop()
        paths.append({"path": list(path)})
    else:
        flights = models.db.session.query(models.Flight).filter_by(source=s).all()
        for flight in flights:
            path[-1]["flight_id"] = flight.id
            path[-1]["duration"] = flight.duration
            path[-1]["departure_day"] = flight.departure_day
            path[-1]["destination"] = flight.destination
            findPaths(flight.destination, d, day, max_flights, paths, path)

    if not path:
        return paths

    path.pop()
    if not path:
        return paths
