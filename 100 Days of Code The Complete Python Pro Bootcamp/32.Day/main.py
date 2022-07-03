import smtplib

my_email = "ibrahimbayburtlu5@gmail.com"
password = "iBo12345*"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() # use security
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
    to_addrs="ibrahimbayburtluweb3learning@gmail.com",
    msg="Subject:Hello\n\nThis is the body of my email.")



