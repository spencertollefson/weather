This repo is for a script I created I believe with the guidance and tutelage of Al Sweigart's *Automate the Boring Stuff*.

Using an API Key, it pulls current and forecasted weather information from openweathermap.org and outputs the information in the terminal. It allows for the user to search any city in the world for which openweathermap.org has that information.

To get started, one will need to setup a file named 'config.py' within the same directory as the repo. The file should contain only the information below, except with the actual weather API the user has obtaine dfrom openweathermap.org:

login = {
    'weather_api': 'ENTER-API-HERE-WITHIN-QUOTES',
}

Further information will be published here later regarding how to run the script. I currently have created an alias "weather" and run this from my CLI by inputting "weather CITY-NAME".