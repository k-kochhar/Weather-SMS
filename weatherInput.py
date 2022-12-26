import requests
import vault

API_KEY = vault.weatherAPIKEY


def weatherData(cred):
# Establishes location based on Google Form input
    city = cred[1]
    state = cred[2]
    country_code = 'US'

# Make the API call to the OpenWeatherMap API
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country_code}&&appid={API_KEY}')

# Check the status code of the response to make sure the request was successful
    if response.status_code == 200:
    # If the request was successful, parse the JSON data from the response
        data = response.json()
        weather = data['weather'][0]['main']
        temperature = (data['main']['temp'])/10
        return [weather, temperature]
    else:
    # If the request was not successful, print an error message and return an Error flag
        print(f'Error {response.status_code}: Could not get weather data for {city}.')
        return[-1, -1]


