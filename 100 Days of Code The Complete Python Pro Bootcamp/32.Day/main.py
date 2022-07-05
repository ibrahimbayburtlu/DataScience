import datetime as dt
import smtplib
import pandas as pd
import random 
import smtplib

MY_EMAIL = "ibrahimbayburtlu5@gmail.com"
MY_PASSWORD = "*******"


today = dt.datetime.now()
today_tuple = (today.month,today.day)

data = pd.read_csv("32.Day/birthdays.csv")
# birthdays_dict = {key:value}
birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birtdays_person = birthdays_dict[today_tuple]
    file_path = f"32.Day/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_contents = contents.replace("[NAME]",birtdays_person["name"])

    with smtplib.SMTP("stmp.gmail.com",port=535) as connection:
        connection.starttls()
        connection. login(MY_EMAIL,MY_PASSWORD)
        connection.send(from_addr = MY_EMAIL,to_addr = birtdays_person["email"],msg=f"Subject:Happy Birthday!\n\n{new_contents}")
    