import streamlit as st
import plotly.express as px

class WeatherView:
    """
    A class that handles the user interface for the weather forecast application.
    """

    @staticmethod
    def display_title():
        """
        Displays the main title of the application.
        """
        st.title("Weather Forecast for the Next Days")

    @staticmethod
    def get_user_input():
        """
        Gathers user input for the city, number of forecast days,
        and the type of data (Temperature or Sky) to display.

        Returns:
            tuple: A tuple containing the city name, number of forecast days,
                   and selected data type (Temperature/Sky).
        """
        # Input field for the city
        place = st.text_input("Place:", help="Enter the name of the city to forecast")

        # Slider for selecting the number of days to forecast
        days = st.slider(
            "Forecast Days",
            min_value=1,
            max_value=5,
            help="Select the number of days you want the weather to be forecasted for"
        )

        # Dropdown for selecting data type (Temperature or Sky)
        option = st.selectbox(
            "Select data to view",
            ("Temperature", "Sky"),
            help="Choose whether to view temperature trends or sky conditions"
        )

        return place, days, option

    @staticmethod
    def display_temperature_chart(temp_data):
        """
        Displays a line chart of temperature trends over time.

        Args:
            temp_data (list of dict): A list of dictionaries containing
                                      date and temperature values.
        """
        # Extract dates and temperatures from the data
        dates = [item["date"] for item in temp_data]
        temps = [item["temp"] for item in temp_data]

        # Create a line chart using Plotly
        figure = px.line(
            x=dates,
            y=temps,
            labels={"x": "Date", "y": "Temperature (°C)"},
            title="Temperature Trends"
        )

        # Render the chart in the Streamlit app
        st.plotly_chart(figure)

    @staticmethod
    def display_sky_images(sky_data, images):
        """
        Displays sky condition images for each forecasted time period.

        Args:
            sky_data (list of dict): A list of dictionaries containing
                                     date and sky condition values.
            images (dict): A dictionary mapping sky condition names
                           (e.g., 'Clear', 'Clouds') to image file paths.
        """
        # Extract sky conditions from the data
        conditions = [item["sky"] for item in sky_data]

        # Map sky conditions to corresponding image paths
        image_paths = [images.get(condition, "images/default.png") for condition in conditions]

        # Display the images in a horizontal format
        st.image(image_paths, width=115, caption=conditions, use_column_width=False)

    @staticmethod
    def display_error(message):
        """
        Displays an error message in the Streamlit app.

        Args:
            message (str): The error message to display.
        """
        st.error(message)
