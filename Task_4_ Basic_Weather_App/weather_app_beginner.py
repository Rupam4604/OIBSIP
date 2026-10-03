# #### *TASK 4 · Basic Weather App*

# ***Objective:** Build a Python application that fetches and displays real-time weather data for a user-specified location using a weather API. Beginners build a command-line tool; advanced builds a graphical app with forecasts and visual elements.*
# ***Tech Stack — Beginner:** Python, `requests`, `json`, OpenWeatherMap API (free tier) **Tech Stack — Advanced:** Python, `requests`, `tkinter` or `PyQt5`, `PIL`/`Pillow` for icons, OpenWeatherMap API*
# ***Feature Checklist — Beginner Tier:***

# - *[ ] Prompt user to enter a city name or ZIP code*
# - *[ ] Make an API call to OpenWeatherMap (or equivalent free API) and parse the JSON response*
# - *[ ] Display: current temperature (°C and °F), humidity percentage, weather condition description (e.g., "Partly Cloudy"), wind speed*
# - *[ ] Handle API errors gracefully: city not found, network timeout, invalid API key*
# - *[ ] Input validation: reject empty city input*

# ***Feature Checklist — Advanced Tier (includes all Beginner features, plus):***

# - *[ ] GUI window with a city input field, a "Get Weather" button, and a results panel*
# - *[ ] Display weather icons corresponding to the current condition (use OpenWeatherMap icon URLs)*
# - *[ ] Hourly forecast panel: show weather for the next 6 hours*
# - *[ ] Daily forecast panel: show weather for the next 5 days*
# - *[ ] Unit toggle: Celsius / Fahrenheit switch button*
# - *[ ] (Bonus) Automatic location detection using the user's IP address via `ipinfo.io` API (free tier)*
# - *[ ] Error messages shown inside the GUI (not terminal print statements)*

# ***Self-Sourcing Guideline:** Register for a **free API key** at openweathermap.org — the free tier allows 60 calls/minute and is sufficient for this project. Search **"Python weather app OpenWeatherMap API tutorial"** on YouTube. Reference the OpenWeatherMap API documentation for JSON response structure. For the GUI version, search **"Python tkinter weather app tutorial"**.*





import requests
import config


 
# FUNCTION: get_weather()
# Purpose:
# Ask the user for a city/ZIP code,
# send a request to OpenWeatherMap,
# and display the weather information.
 
def get_weather():

    # Keep asking until the user enters a valid location
    while True:

        # Ask the user to enter a city name or ZIP code
        location = input("Enter city name or ZIP code: ").strip()

        # Check whether the user entered nothing
        if not location:
            print("Error: City name or ZIP code cannot be empty.")
            print("Please try again.\n")
            continue

        # A valid location was entered
        break

     
    # GET API KEY
     

    # Get the API key from config.py
    # strip() removes accidental spaces before/after the key
    api_key = config.api_key.strip()

     
    # CREATE API URL
     

    # If the user entered only numbers,
    # we assume it is a ZIP code.
    if location.isdigit():

        # ZIP code request
        # IN = India
        api_url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?zip={location},IN"
            f"&appid={api_key}"
            f"&units=metric"
        )

    else:

        # City name request
        api_url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={location}"
            f"&appid={api_key}"
            f"&units=metric"
        )

     
    # SEND REQUEST TO OPENWEATHERMAP
     

    try:

        # Send a GET request to the API
        # timeout=10 means Python will wait
        # maximum 10 seconds for a response
        response = requests.get(api_url, timeout=10)

         
        # CHECK API ERRORS
         

        # 401 means the API key is invalid
        if response.status_code == 401:
            print("Error: Invalid API key.")
            return

        # 404 means the city/ZIP code was not found
        if response.status_code == 404:
            print("Error: Location not found.")
            return

        # Check for any other HTTP error
        response.raise_for_status()

         
        # CONVERT JSON INTO PYTHON DICTIONARY
         

        # OpenWeatherMap sends data in JSON format.
        # response.json() converts that JSON into
        # a Python dictionary.
        data = response.json()

         
        # EXTRACT WEATHER INFORMATION
         

        # Get city name
        city_name = data["name"]

        # Get temperature in Celsius
        temperature_c = data["main"]["temp"]

        # Get humidity percentage
        humidity = data["main"]["humidity"]

        # Get weather description
        description = data["weather"][0]["description"]

        # Get wind speed
        wind_speed = data["wind"]["speed"]

         
        # CONVERT CELSIUS TO FAHRENHEIT
         

        temperature_f = (temperature_c * 9 / 5) + 32

         
        # DISPLAY WEATHER INFORMATION
         

        print("\n" + "=" * 40)
        print(f"Weather for {city_name}")
        print("=" * 40)

        print(f"Temperature : {temperature_c:.2f} °C")
        print(f"Temperature : {temperature_f:.2f} °F")
        print(f"Humidity    : {humidity}%")
        print(f"Condition   : {description.title()}")
        print(f"Wind Speed  : {wind_speed} m/s")

        print("=" * 40)

     
    # HANDLE NETWORK TIMEOUT
     

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        print("Please check your internet connection and try again.")

     
    # HANDLE INTERNET CONNECTION ERROR
     

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the weather server.")
        print("Please check your internet connection.")

     
    # HANDLE OTHER REQUEST ERRORS
     

    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")


 
# MAIN PROGRAM
 

# Keep the program running so the user can
# check the weather for multiple locations.
while True:

    # Call our weather function
    get_weather()

    # Ask whether the user wants another search
    choice = input(
        "\nDo you want to check another location? (y/n): "
    ).strip().lower()

    # If the user doesn't enter "y",
    # close the program.
    if choice != "y":
        print("Weather App closed.")
        break

    # Add an empty line before the next search
    print()