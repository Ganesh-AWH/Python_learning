import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
APPID = "699c035166068fdc4b7d9d2d002bd95b"
#twilio id
account_sid = "id"
auth_token = "token"

parameters = {
    "lat" : -4.441931,
    "lon" : 15.266293,
    "appid" : APPID,
    "cnt" : 4
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data['list'][0]['weather'][0]['id'])

will_rain = False
for hour_data in weather_data['list']:
    condition_code = int(hour_data['weather'][0]['id'])
    if condition_code < 700:
        will_rain = True
    
if will_rain:
    # print("Bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body='It is going to rain, Bring an umbrella',
    from_='+13344384439',
    to='+917010799778',
    )
    print(message.status)