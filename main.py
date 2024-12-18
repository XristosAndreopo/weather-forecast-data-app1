import streamlit as sl
import plotly.express as px

from backend import get_data

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

if place:
    #if place doesn't exist
    try:
        #Get the temperature/sky data
        filtered_data = get_data(place, days)

        #Create a temperature plot
        if option == "Temperature":
            #get the temperatures only by get_data()
            filtered_temp = [diction["main"]["temp"]/10 for diction in filtered_data]
            #get the days only by get_data()
            filtered_days = [diction["dt_txt"] for diction in filtered_data]
            #Create the plot
            figure = px.line(x=filtered_days, y=filtered_temp,
                             labels={"x": "Date", "y": "Temperature (C)"})
            sl.plotly_chart(figure)

        #Create a Sky plot
        if option == "Sky":
            # get the sky data only by get_data()
            sky = [diction["weather"][0]["main"] for diction in filtered_data]
            #create my_dictionary with sky names and image paths
            images={"Clear": "images/clear.png", "Clouds": "images/clouds.png",
                         "Rain": "images/rain.png", "Snow": "images/snow.png"}
            #create list with image paths
            image_paths =[images[condition] for condition in sky]
            #print images
            sl.image(image_paths, width=115)

    except KeyError:
        sl.write("This place doesnt exist")
