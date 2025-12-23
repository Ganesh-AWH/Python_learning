import requests
from datetime import datetime

GENDER = "M"
WEIGHT = 65
HEIGHT = 170
AGE = 22


APP_ID = "your api id"
APP_KEY = "your api key"
sheet_endpoint = "https://api.sheety.co/6f2297baded3ea0a90cd44882a906967/copyOfMyWorkouts/workouts"

TOKEN = "your token"

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY,
}
exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise" 
# exercise_input = input("tell me which exercise you perform today? ")
parameters = {
    "query" : "I lifted 200kg today",
    "weight_kg" : WEIGHT,
    "hieght_cm" : HEIGHT,
    "age" : AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

#google spread sheet adding new data using api
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
bearer_headers = {
"Authorization": f"Bearer {TOKEN}"
}
for exercise in result['exercises']:
    sheet_inputs = {
        "workout" : {
            "date" : today_date,
            "time" : now_time,
            "exercise" : exercise['name'].title(),
            "duration" : exercise['duration_min'],
            "calories" : exercise['nf_calories'],
        }
    }
    sheet_response = requests.post(
        url=sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers)
    print(sheet_response.text)