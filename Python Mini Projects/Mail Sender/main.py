import smtplib

MY_EMAİL = "ibrahimbayburtlu5@gmail.com"
MY_PASSWORD = "iBo12345*"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAİL,password=MY_PASSWORD)