import requests
import pandas as pd

# Stockholm coordinates
latitude = 59.3293
longitude = 18.0686

# API URL
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max&timezone=auto"

# Request data from API
response = requests.get(url)

# Convert response to JSON
data = response.json()

import json

with open("raw_data/stockholm_weather.json", "w") as file:
    json.dump(data, file, indent=4)

print("Weather data saved successfully!")
