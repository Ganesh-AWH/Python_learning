import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response)

response.raise_for_status()
print(response.status_code)

data = response.json()
print(data)

longititude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(longititude)
print(latitude)