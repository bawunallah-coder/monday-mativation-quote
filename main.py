import datetime as dt
import random
import smtplib
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
week_day=now.weekday()

if week_day==0:
    with open("quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote=random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivational Quote\n\n{quote}."
                            )
