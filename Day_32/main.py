import smtplib
import datetime as dt
import random


def send_mail():
    my_email = "jason.python.learning@gmail.com"
    my_password = "tkjbmjnixscpataf"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        quote = random.choice(quotes)
    send_mail()

