import requests

class WeatherData:
    # Paste your own API KEY
    API_KEY = "e836ed8094f91e6ff3bb33410b58586c"
    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

    def __init__(self, place, forecast_days):
        self.place = place
        self.forecast_days = forecast_days

    def fetch_data(self):
        """
        Get data from API for specific days.
        :return: Data from API for specific days.
        """
        url = f"{self.BASE_URL}?q={self.place}&appid={self.API_KEY}"
        # Requesting data from API.
        response = requests.get(url)
        if response.status_code == 200:
            # Make data to json.
            data = response.json()
            # Multiply by 8 because each row in dictionary has an interval of 3 hours
            # so 8 * 3 = 24 hours.
            # Get the data for selected days.
            return data["list"][: self.forecast_days * 8]
        else:
            # If status_code doesn’t lie in range of 200-29 print the status code.
            raise ValueError(f"Error fetching data: {response.status_code}")

    def get_temperature_data(self):
        """
        Get the temperature of selected days.
        :return: List of dictionaries with dates and temperatures.
        """
        # Data from API for specific days.
        data = self.fetch_data()
        return [
            {"date": item["dt_txt"], "temp": item["main"]["temp"] - 273.15}
            for item in data
        ]

    def get_sky_data(self):
        """
        Get the sky of selected days.
        :return: List of dictionaries with dates and sky.
        """
        # Data from API for specific days.
        data = self.fetch_data()
        return [{"date": item["dt_txt"], "sky": item["weather"][0]["main"]} for item in data]
