import streamlit as sl

#Create title of Data app
sl.title("Weather Forecast for the Next Days")

#Create input for city for forecast
place = sl.text_input("Place: ")

#Create slider for number of forecasted days
days = sl.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the numbers of days you want to be"\
                      "forecasted")

#Create select box for Temperature/Sky
option = sl.selectbox("Select data to view", ("Temperature", "Sky"))

#Create dynamic sub header
sl.subheader(f"{option} for the next {days} days in {place}")