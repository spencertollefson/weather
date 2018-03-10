"""Created on 12-Feb-18.
Author: Spencer Tollefson
Description: weather.py - Prints current weather and forecast for
next 10 days from OpenWeatherMap.org based on CLI location
"""

import json
import requests
import sys
import config
import pprint

# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: weather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.

#comment out either or for testing
url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&mode=json&units=imperial&APPID='\
      + config.login['weather_api']
#####url = f'http://api.openweathermap.org/data/2.5/weather?q=seattle&mode=json&units=imperial&APPID='\
#####      + config.login['weather_api']

# API_KEY d3db0da25150323093a4d1f8eb275fd7

response = requests.get(url)
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print('Check that location was spelled and formatted quickly. EX: Seattle, US')

# Load JSON data into a Python variable
weatherData = json.loads(response.text)
#pprint.pprint(weatherData)

# Print current weather descriptions
print('Current weather in', weatherData['name']+',', weatherData['sys']['country']+':')
print(weatherData['main']['temp'], 'degrees F -', 'Description: '
      + weatherData['weather'][0]['main']+'>>', weatherData['weather'][0]['description'],
      '-- Wind speed:', weatherData['wind']['speed'], 'mph')
print('')

"""Now the focus is on the future weather conditions"""

# Load data for future times into requests object
future_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&mode=json&units=imperial&APPID='\
             + config.login['weather_api']
#####future_url = f'http://api.openweathermap.org/data/2.5/forecast?q=seattle&mode=json&units=imperial&APPID='\
#####             + config.login['weather_api']

future_response = requests.get(future_url)

# Try to access the API for the future weather data
try:
    future_response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print('Check that location was spelled and formatted quickly. EX: Seattle, US')

futureWeatherData = json.loads(future_response.text)

# Print future weather descriptions

print('3 hour interval forecast')
for segment in futureWeatherData['list']:
    print(segment['dt_txt'], '- ', segment['main']['temp'], 'degrees F', ' - Description:', segment['weather'][0]['description'])