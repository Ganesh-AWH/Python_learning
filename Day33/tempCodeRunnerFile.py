import requests
MY_LAT = 20.593683
MY_LONG = 78.962883
# response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response)

# response.raise_for_status()
# print(response.status_code)

# data = response.json()
# print(data)

# longititude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# print(longititude)
# print(latitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
