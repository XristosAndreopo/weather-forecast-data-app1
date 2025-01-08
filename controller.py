from backend import WeatherData
from view import WeatherView

class WeatherController:
    """
    A controller class that coordinates between the backend (data fetching)
    and the view (user interface) for the weather forecast application.
    """

    def __init__(self):
        """
        Initializes the WeatherController with an instance of WeatherView.
        """
        self.view = WeatherView()

    def run(self):
        """
        The main method to run the application. Handles user inputs,
        fetches weather data from the backend, and displays results
        through the view.
        """
        # Display the application title
        self.view.display_title()

        # Get user input: place, number of forecast days, and data type
        place, days, option = self.view.get_user_input()

        # If the user has entered a place, proceed to fetch and display data
        if place:
            try:
                # Create an instance of WeatherData with the user's inputs
                weather = WeatherData(place, days)

                # Handle temperature data visualization
                if option == "Temperature":
                    # Fetch temperature data from the backend
                    temp_data = weather.get_temperature_data()

                    # Pass the data to the view for visualization
                    self.view.display_temperature_chart(temp_data)

                # Handle sky condition visualization
                elif option == "Sky":
                    # Fetch sky condition data from the backend
                    sky_data = weather.get_sky_data()

                    # Map sky condition names to image file paths
                    images = {
                        "Clear": "images/clear.png",
                        "Clouds": "images/clouds.png",
                        "Rain": "images/rain.png",
                        "Snow": "images/snow.png",
                    }

                    # Pass the data and image mappings to the view for display
                    self.view.display_sky_images(sky_data, images)

            except ValueError as e:
                # Display an error message if there's an issue fetching data
                self.view.display_error(str(e))
