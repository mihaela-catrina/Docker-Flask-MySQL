import sys
# importing the requests library
import requests

print("Comanda adugare zbor: adaugaZbor(id, sursa, destinatie, ....)")
print("Comanda sterge zbor: stergeZbor(id)")

# api-endpoint
URL_ADAUGA_ZBOR = "http://managemenet_server:5000/add_flight"

while True:
    inp = input("Apasa 1 pentru adaugare zbor / 2 pentru stergere zbor: ")
    if inp == "1":
        id = input("ID zbor")
        source = input("Sursa zbor: ")
        destination = input("Distinatie zbor: ")
        departure_day = input("Departure day [1-365]: ")
        departure_hour = input("Departure hour [0 - 23]")
        duration = input("Duration: ")
        seats = input("Seats: ")

        PARAMS = {
            "source": source,
            "destination": destination,
            "departureDay": int(departure_day),
            "departureHour": int(departure_hour),
            "duration": int(duration),
            "seats": int(seats),
            "id": int(id)
        }

        resp = requests.post(URL_ADAUGA_ZBOR, data=PARAMS)
        print(resp.status_code, resp.reason)
