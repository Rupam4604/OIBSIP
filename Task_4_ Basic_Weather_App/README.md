# 🌦️ Task 4 — Basic Weather App

A Python command-line weather application developed as part of the **Oasis Infobyte Python Programming Internship (OIBSIP)**.

The application fetches real-time weather information from the **OpenWeatherMap API** based on a user-entered city name or ZIP code.

---

## 🎯 Objective

Build a Python application that:

- Accepts a city name or ZIP code
- Fetches real-time weather data using an API
- Parses the JSON response
- Displays important weather information
- Handles common API and network errors
- Validates user input

---

## 🟢 Beginner Version

### Features

- 🌍 Enter city name or ZIP code
- 🌐 OpenWeatherMap API integration
- 🌡️ Temperature in Celsius
- 🌡️ Temperature in Fahrenheit
- 💧 Humidity percentage
- ☁️ Weather condition
- 💨 Wind speed
- ⚠️ Invalid API key handling
- 🔍 Location not found handling
- ⏱️ Network timeout handling
- ❌ Empty input validation
- 🔄 Check multiple locations in one session

---

## 🛠️ Technologies Used

- Python
- `requests`
- JSON
- OpenWeatherMap API

---

## 📁 Project Structure

```text
Task_4_Basic_Weather_App/
│
├── weather_app_beginner.py
├── config.py
├── .gitignore
└── README.md