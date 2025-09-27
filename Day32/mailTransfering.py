import smtplib

my_mail = "anonymouswhitehack746@gmail.com"
password = "bsdx mxcb rkvn hxhm"



with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail, to_addrs="ganesh02003@gmail.com", msg="Subject:Hello\n\nI am from body message")