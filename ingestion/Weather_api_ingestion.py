import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "weather-raw"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

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
    blob_name = f"{city}_weather_{today_date}.json"

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )

    with open(file_path, "rb") as data_file:
        blob_client.upload_blob(data_file, overwrite=True)

    print(f"{city} weather data uploaded to Azure Blob Storage!")

