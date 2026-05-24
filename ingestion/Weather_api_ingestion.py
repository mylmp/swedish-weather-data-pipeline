import requests
import json
from datetime import datetime

cities = {
    "stockholm": {"latitude": 59.3293, "longitude": 18.0686},
    "gavle": {"latitude": 60.6749, "longitude": 17.1413},
    "lulea": {"latitude": 65.5848, "longitude": 22.1547}
}

today_date = datetime.today().strftime("%Y-%m-%d")

for city, coordinates in cities.items():
    latitude = coordinates["latitude"]
    longitude = coordinates["longitude"]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max&timezone=auto"

    response = requests.get(url)
    data = response.json()

    file_path = f"raw_data/{city}_weather_{today_date}.json"

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print(f"{city} weather data saved successfully!")
    