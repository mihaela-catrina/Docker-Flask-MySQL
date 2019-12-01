import sys
import requests

# api-endpoint
URL_ADAUGA_ZBOR = "http://managemenet_server:5000/add_flight"
URL_STERGE_ZBOR = "http://managemenet_server:5000/remove_flight"
URL_BOOK_TICKET = "http://flight_service:6000/book_flights"
URL_BUY_TICKET = "http://flight_service:6000/buy_ticket"
URL_GET_OPTIMAL_PATH = "http://flight_service:6000/get_optimal_path"

while True:
    print("""Commands:
Press 1 to add a new flight
Press 2 to remove an existing flight
Press 3 to book a ticket
Press 4 to buy a ticket (First make reservation)
Press 5 to find an optimal route""")
    inp = input("Your Command: ")
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
            print("\n")

    if inp == "2":
        id = input("Flight ID: ")

        PARAMS = {
            "id": id
        }
        resp = requests.post(URL_STERGE_ZBOR, data=PARAMS)
        print(resp.status_code, resp.json())
        print("\n")


    if inp == "3":
        ids = input("Flight IDs (e.g. 1,3,4): ")

        PARAMS = {
            "flight_ids": ids
        }
        resp = requests.post(URL_BOOK_TICKET, data=PARAMS)
        print(resp.status_code, resp.json())
        print("\n")


    if inp == "4":
        id = input("Reservation ID: ")

        PARAMS = {
            "reservation_id": id
        }
        resp = requests.post(URL_BUY_TICKET, data=PARAMS)
        print(resp.status_code, resp.json())
        print("\n")


    if inp == "5":
        source = input("Source: ")
        destination = input("Destination: ")
        departure_day = input("Departure day [1-365]: ")
        max_flights = input("Max Flights: ")

        ok = True
        try:
            PARAMS = {
                "source": source,
                "destination": destination,
                "departure_day": int(departure_day),
                "max_flights": int(max_flights)
            }
        except Exception as e:
            ok = False
            print("""Incorrect information inserted\n
Departure Day should be an integer between 1 and 365\n
Max Flights should be an integer between 0 and 23\n
""")

        if ok:
            resp = requests.post(URL_GET_OPTIMAL_PATH, data=PARAMS)
            json_rsp = resp.json()
            paths = json_rsp['paths']
            if paths is None or len(paths) == 0:
                print("!!!! We can't find you a route! Sorry! Try other flights!")
                continue

            ids = []
            for path in paths:
                print("Source:", path["source"], "-", "Destination:", path['destination'], "-", "Departure Day:",
                      path["departure_day"], "-", "Departure Hour:", path['departure_hour'], "-", "Duration:", path['duration'],
                      "-", "Flight ID:", path["flight_id"])
                ids.append(path['flight_id'])
            print("Flights IDs:")
            for id in ids:
                print(id)
            print("\n")
