import requests

#constant value
API_KEY = "e836ed8094f91e6ff3bb33410b58586c"

def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    #requesting data from API
    response = requests.get(url)
    #make data to json
    data = response.json()
    #get specific data
    filtered_data = data["list"]
    #multilpy by 8 because each row in dictionary has an interval of 3 hours
    #so 8 * 3 = 24 hours
    nr_values = 8 * forecast_days
    #get the data for selected days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))