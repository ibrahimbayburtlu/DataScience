import random
length = int(input("enter the length of password:"))

letter = "qwertyuıopğüasdfghjklşi,zxcvbnmöç.1234567890*-"

password = ""



for i in range(length):
    password += random.choice(letter)

print(password)