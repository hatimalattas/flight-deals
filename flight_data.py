from datetime import datetime


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, search_result):
        self.search_result = search_result
        self.structured_result = []
        self.structure_data(self.search_result)

    def format_date(self, iso_date):
        iso_date_datetime = datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%S.%fZ")

        date_formatted = iso_date_datetime.strftime("%d/%m/%Y")

        return date_formatted

    def structure_data(self, search_result):
        for result in search_result:
            self.structured_result.append({
                "price": result["price"],
                "city_from": result["cityFrom"],
                "fly_from": result["flyFrom"],
                "city_to": result["cityTo"],
                "fly_to": result["flyTo"],
                "departure": self.format_date(result["local_departure"]),
                "arrival": self.format_date(result["local_arrival"])
            })
