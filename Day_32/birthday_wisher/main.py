from datetime import datetime
import pandas
import random
import smtplib

my_email = "jason.python.learning@gmail.com"
my_password = "tkjbmjnixscpataf"

today_tuple = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    name = birthday_person["name"]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", name)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person.email,
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )
