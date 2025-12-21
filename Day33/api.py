import requests

# response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response)
# j_data = response.json()
# print(j_data["iss_position"]["latitude"])
# print(j_data["iss_position"]["longitude"])


response = requests.get("https://api.sunrise-sunset.org/json", apid="339363df47a4c2a9585998fbde4eb8c0")
print(response)
sun_rise = response.json()["results"]["sunrise"]
sun_set = response.json()["results"]["sunset"]
print(sun_rise)
print(sun_set)
#nltk operations

