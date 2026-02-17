# api_tutorial.py
import requests

URL = "http://api.open-notify.org/astros.json"

response = requests.get(URL)
print("Status code:", response.status_code)

data = response.json()

# print("\n--- Raw JSON (Python dict) ---")
# print(data)

print("\n--- Formatted Output ---")
print(f"People in space: {data.get('number')}")
for person in data.get("people", []):
    # prints like: ISS: Oleg Kononenko
    print(f"{person.get('craft')}: {person.get('name')}")