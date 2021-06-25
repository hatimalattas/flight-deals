import requests


class DataManager:
    def __init__(self):
        # This class is responsible for talking to the Google Sheet.
        sheety_endpoint = "https://api.sheety.co/78a0330841caf9eb95c180ed1e5e1bbd/flightDeals/prices"
        self.response = requests.get(url=sheety_endpoint)
        self.response.raise_for_status()
