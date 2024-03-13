import requests
import os
import json
from found_flight import FoundFlight
import datetime

API_KEY = os.environ.get("KIWI_API_KEY")
KIWI_END_POINT = "https://tequila-api.kiwi.com"
header = {
    "apikey": API_KEY
}
# The below line is for testing purpose of the response
# with open("reponse_json.txt",mode="w") as file:
#     writing = file.write(f"{response}")

class SearchFlight:
     def search_flight(self, fly_from, fly_to, date_from : datetime, date_to: datetime):
        flight_data = {}
        parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"   
        }

        response = requests.get(url = f"{KIWI_END_POINT}/v2/search", params = parameters, headers = header)
        try:
            flight_data = response.json()["data"][0]
        except IndexError:
            print("No flights in the search criteria")
        except KeyError:
            pass
        if len(flight_data): # If any flight is found then all details passes to FoundFlight object.
            new_found_flight = FoundFlight(
            price_to = flight_data["price"],
            city_from = flight_data["route"][0]["cityFrom"],
            fly_from = flight_data["route"][0]["flyFrom"],
            city_to = flight_data["route"][0]["cityTo"],
            fly_to = flight_data["route"][0]["flyTo"],
            date_from = flight_data["route"][0]["local_departure"].split("T")[0],
            date_to = flight_data["route"][1]["local_departure"].split("T")[0]
        )
            return new_found_flight
        else:
            print("No flights in the search criteria")
            