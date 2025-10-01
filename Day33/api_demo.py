import smtplib
import requests
from datetime import datetime
import time

MY_LAT = 20.593683
MY_LONG = 78.962883

MY_MAIL = "anonymouswhitehack746@gmail.com"
MY_PASS = "bsdx mxcb rkvn hxhm"

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longititude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longititude <= MY_LONG+5:
        return True
    
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True

while True: 
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_MAIL, MY_PASS)
            connection.sendmail(
                from_addr=MY_MAIL,
                to_addrs=MY_MAIL,
                msg="Subject: Lookup\n\nThe ISS is above you in the sky"
            )