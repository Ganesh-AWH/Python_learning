import pandas as pd
import random
import smtplib
import datetime as dt

MY_MAIL = "anonymouswhitehack746@gmail.com"
PASSWORD = "bsdx mxcb rkvn hxhm"

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
########################################################################################


#Extrcting birthdays from csv as list of dictionary

df = pd.read_csv(r"E:\Programming\Python\Udemy Course\Day32\Birthday Wisher\birthdays.csv")
birthdays_dict = df.to_dict(orient="records")

#current data
now = dt.datetime.now()
curr_day = now.day
curr_month = now.month
curr_year = now.year


letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
random_file = random.choice(letters)

for details in birthdays_dict:
    if(details["month"] == curr_month and details["day"] == curr_day):
        file_path = fr"E:\Programming\Python\Udemy Course\Day32\Birthday Wisher\letter_templates\{random_file}"
        with open(file_path) as data_file:
            age = curr_year - details["year"] 
            email_content = data_file.read()
            email_content = email_content.replace("[NAME]", details["name"])
            email_content = email_content.replace("[AGE]", str(age))
            
        # sending mail 
        with smtplib.SMTP("smtp.gmail.com") as connection:
            message = f"Subject:Birthday wishes\n\n{email_content}"
            connection.starttls()
            connection.login(user=MY_MAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_MAIL, 
                to_addrs="ganesh02003@gmail.com", 
                msg=message.encode("utf-8")
            )

