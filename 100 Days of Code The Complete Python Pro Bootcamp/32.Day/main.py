import smtplib

my_email = "ibrahimbayburtlu5@gmail.com"
password = "iBo12345*"

with smtplib.SMTP("smtp.gmail.com",port=535) as connection:
    connection.starttls() # use security
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
    to_addrs="ibrahimbayburtluweb3learning@gmail.com",
    msg="Subject:Hello\n\nThis is the body of my email.")



import datetime as dt

now = dt.datetime.now()
if now.year == 2022:
    print("hello world")
day_of_week = now.weekday()
print(day_of_week)
print(now)


date_of_birth = dt.datetime(year=2000,month=11,day=4,hour=12,minute=30)
print(date_of_birth)
