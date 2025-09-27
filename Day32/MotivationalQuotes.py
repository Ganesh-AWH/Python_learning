import datetime as dt
import smtplib
import random

MY_MAIL = "anonymouswhitehack746@gmail.com"
PASSWORD = "bsdx mxcb rkvn hxhm"

#data Extraction from file
file_path = r"E:\Programming\Python\Udemy Course\Day32\quotes.txt"
with open(file_path, encoding="utf-8") as data_file:
    quotes_list = data_file.readlines()

quotes_list = [item.strip() for item in quotes_list]

#Data Extraction
now = dt.datetime.now()
week_num = now.weekday()

#Sending mail
if week_num == 5:
    quote = random.choice(quotes_list)
    message = f"Subject:Quote of the data\n\n{quote}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_MAIL, 
            to_addrs="ganesh02003@gmail.com", 
            msg=message.encode("utf-8")
        )
        