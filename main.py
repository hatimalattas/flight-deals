from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

data_manager = DataManager
flight_search = FlightSearch(data_manager)
flight_data = FlightData(flight_search.search_result)
notification_manager = NotificationManager(flight_data.structured_result)
