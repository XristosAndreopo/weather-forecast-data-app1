

# Weather Forecast Data app

## About The Project
This is a Data visualization app. It takes data from API of "https://api.openweathermap.org" to the data app.
The app displays the forecast weather for selected days.

### Built With
This project was build with:
1) Pycharm 
2) Streamlit
3) Build with MVC architecture

###  Model-View-Controller (MVC):
weather_app/<br />
│<br />
├── backend.py  &emsp;&emsp;# Model: Fetch and process data from the API.<br />
├── view.py&emsp;&emsp;&emsp;&emsp;# View: Handle Streamlit UI components.<br />
├── controller.py&emsp;&emsp;# Controller: Coordinate between backend and view.<br />
├── main.py&emsp;&emsp;&emsp;&emsp;# Entry point: Initialize and run the app.<br />
├── images/&emsp;&emsp;&emsp;&emsp;# Store weather-related images.<br />
└── requirements.txt    # Dependencies (requests, streamlit, plotly).<br />


### Installation

1. Connect to https://api.openweathermap.org, sign in, and get the API_KEY and paste it to backend.py.
2. Clone the repo with the
```sh
  https://github.com/XristosAndreopo/weather-forecast-data-app1.git
   ```
4. pip install -r requirements.txt.
3. Run in terminal the following: streamlit run main.py. 

<!-- CONTACT -->
## Contact Details

Christos - xristos.andreopo@gmail.com

Project Link: https://github.com/XristosAndreopo/weather-forecast-data-app1.git
