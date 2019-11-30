import sys
import requests

# api-endpoint
URL_ADAUGA_ZBOR = "http://managemenet_server:5000/add_flight"
URL_STERGE_ZBOR = "http://managemenet_server:6000/remove_flight"
URL_BOOK_TICKET = "http://flight_service:6000/book_flight"

while True:
    inp = input("Press 1 if you want to add a new flight / 2 to remove an existing flight / 3 to book a ticket: ")
    if inp == "1":
        id = input("Flight ID: ")
        source = input("Source: ")
        destination = input("Destination: ")
        departure_day = input("Departure day [1-365]: ")
        departure_hour = input("Departure hour [0 - 23]: ")
        duration = input("Duration: ")
        seats = input("No Of Seats: ")

        ok = True
        try:
            PARAMS = {
                "source": source,
                "destination": destination,
                "departureDay": int(departure_day),
                "departureHour": int(departure_hour),
                "duration": int(duration),
                "seats": int(seats),
                "id": id
            }
        except Exception as e:
            ok = False
            print("""Incorrect information inserted\n
Flight ID is a string\n
Departure Day should be an integer between 1 and 365\n
Departure Hour should be an integer between 0 and 23\n
Duration should be an integer\n
No Of Seats should be an integer\n
""")

        if ok:
            resp = requests.post(URL_ADAUGA_ZBOR, data=PARAMS)
            print(resp.status_code, resp.json())

    if inp == "2":
        id = input("Flight ID: ")

        PARAMS = {
            "id": id
        }
        resp = requests.post(URL_STERGE_ZBOR, data=PARAMS)
        print(resp.status_code, resp.json())

    if inp == "3":
        id = input("Flight ID: ")

        PARAMS = {
            "flight_id": id
        }
        resp = requests.post(URL_BOOK_TICKET, data=PARAMS)
        print(resp.status_code, resp.json())
