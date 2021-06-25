import requests
import datetime
import math

FLY_FROM = "JED"
CURRENCY = "SAR"
SORT = "price"

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
after_six_months = tomorrow + datetime.timedelta(days=180)


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self, data_manager):
        self.data_manager = data_manager()
        self.flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.tomorrow_formatted = tomorrow.strftime("%d/%m/%Y")
        self.after_six_months_formatted = after_six_months.strftime("%d/%m/%Y")
        self.parameters = {
            "fly_from": FLY_FROM,
            "fly_to": None,
            "date_from": self.tomorrow_formatted,
            "date_to": self.after_six_months_formatted,
            "price_to": None,
            "curr": CURRENCY,
            "sort": SORT,
        }

        self.sheet_data = self.data_manager.response.json()["prices"]

        self.headers = {
            "apikey": "v8j3D6YpQVKtNNWUhKwEKSqh2NM4BgNf"
        }
        self.search_result = []

        self.search(self.sheet_data)

    def search(self, sheet_data):
        for row in sheet_data:
            self.parameters["fly_to"] = row["iataCode"]
            self.parameters["price_to"] = math.ceil(row["lowestPrice (sar)"])

            response = requests.get(url=self.flight_search_endpoint, params=self.parameters, headers=self.headers)
            response.raise_for_status()

            if len(response.json()["data"]) > 0:
                self.search_result.append(response.json()["data"][0])
