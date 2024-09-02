import random
import smtplib
import datetime as dt

target_mail = "balaji.balachandar1@gmail.com"
my_mail = "sampleforpythonmail@gmail.com"
# password from app password option
password = ""

with open("quotes.txt") as data:
    list_of_quotes = data.readlines()

random_quote = random.choice(list_of_quotes)

monday = 0
today = dt.datetime.now()
week_day = today.weekday()

if week_day == monday:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_mail,password=password)
        connection.sendmail(from_addr=my_mail,
                            to_addrs=target_mail,
                            msg=f"Subject:Quote of the day\n\n{random_quote}")
