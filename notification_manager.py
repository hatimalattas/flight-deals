class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, structured_data):
        self.structured_data = structured_data
        self.send_notification(self.structured_data)

    def send_notification(self, structured_data):
        for data in structured_data:
            print(f"Low price alert! Only {data['price']} SAR to fly from {data['city_from']}-{data['fly_from']} to "
                  f"{data['city_to']}-{data['fly_to']}, from {data['departure']} to {data['arrival']}")
