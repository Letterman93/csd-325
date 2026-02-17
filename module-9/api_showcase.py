# my_api_program.py
import json
import requests

URL = "https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&current_weather=true"

# 1) Test connection
response = requests.get(URL)
print("Status code:", response.status_code)

# 2) Print raw response (unformatted)
print("\n--- Raw Response ---")
print(response.text)

# 3) Print formatted JSON (clean + indented)
data = response.json()

print("\n--- Formatted JSON ---")
print(json.dumps(data, indent=4))

# Optional clean summary line
current = data.get("current_weather", {})
print("\n--- Simple Summary ---")
print(f"Temperature: {current.get('temperature')}°C")
print(f"Windspeed: {current.get('windspeed')} km/h")