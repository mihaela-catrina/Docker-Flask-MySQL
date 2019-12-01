from app import models
from app import graph


def verify_overbooking(flight_id, bookings):
    try:
        obj = models.db.session.query(models.Flight).filter_by(id=flight_id).one()
        seats = obj.seats
        overload = (seats * 11) / 10
        x = (bookings > overload)
        return x
    except Exception as _:
        return True


def book_flights(flight_ids):
    try:
        flight_ids_list = [x.strip() for x in flight_ids.split(',')]
        bookings = models.Booking.query.all()
        for flight_id in flight_ids_list:
            count = 0
            for book in bookings:
                book_flight_ids = [x.strip() for x in book.flight_ids.split(',')]
                if flight_id in book_flight_ids:
                    count = count + 1
            rsp = verify_overbooking(flight_id, count)
            if rsp is True:
                return 0
        booking = models.Booking(flight_ids=flight_ids)
        models.db.session.add(booking)
        models.db.session.commit()
        return booking.id
    except Exception as _:
        return 0


def buy_ticket(reservation_id):
    try:
        obj = models.db.session.query(models.Booking).filter_by(id=reservation_id).one()
        if obj:
            ticket = models.Ticket(reservation_id=reservation_id)
            models.db.session.add(ticket)
            models.db.session.commit()
            return 1
        return 0
    except Exception as _:
        return 0


def verify_consistency(path, day, max_flights):

    if len(path) > max_flights:
        return False

    if path[0]["departure_day"] != day:
        return False

    for i in range(len(path)):
        if i == 0:
            continue
        previous_departure_day = path[i-1]["departure_day"]
        previous_departure_hour = path[i-1]["departure_hour"]
        previous_duration = path[i-1]["duration"]
        current_departure_day = path[i]["departure_day"]
        current_departure_hour = path[i]["departure_hour"]
        if previous_departure_day > current_departure_day:
            return False

        prev_arrival_day = previous_departure_day + ((previous_departure_hour + previous_duration) // 24)
        prev_arrival_hour = ((previous_departure_hour + previous_duration) % 24)
        if prev_arrival_day > current_departure_day:
            return False
        if prev_arrival_day == current_departure_day and prev_arrival_hour > current_departure_hour:
            return False

    return True


def findPaths(s, d, day, max_flights, paths):
    flights = models.db.session.query(models.Flight).filter_by(source=s).all()
    for flight in flights:
        path = []
        paths_aux = []
        paths_aux = findPathsUtil(flight, d, day, max_flights, paths_aux, path)
        paths = paths + paths_aux

    return paths


def findPathsUtil(flight_s, dst, day, max_flights, paths, path):

    dict = {}
    dict["source"] = flight_s.source
    dict["flight_id"] = flight_s.id
    dict["duration"] = flight_s.duration
    dict["departure_day"] = flight_s.departure_day
    dict["departure_hour"] = flight_s.departure_hour
    dict["destination"] = flight_s.destination
    path.append(dict)

    if flight_s.destination == dst:
        if verify_consistency(path, day, max_flights):
            paths.append({"path": list(path)})
    else:
        flights = models.db.session.query(models.Flight).filter_by(source=flight_s.destination).all()
        for flight in flights:
            findPathsUtil(flight, dst, day, max_flights, paths, path)

    path.pop()
    if not path:
        return paths


def get_optimal_route(source, dest, max_flights, dep_day):
    paths = []
    paths = findPaths(source, dest, dep_day, max_flights, paths)

    best_path = None
    max_val = 99999999
    for path_a in paths:
        path = path_a["path"]
        pth_l = len(path) - 1
        time = (path[pth_l]["departure_day"] - path[0]["departure_day"]) * 24 + (path[pth_l]["departure_hour"] + path[pth_l]["duration"] - path[0]["departure_hour"])
        if time < max_val:
            max_val = time
            best_path = path

    return best_path
