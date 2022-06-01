# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first_number = int(two_digit_number) % 10
second_number = int(int(two_digit_number) / 10)

print(first_number + second_number) 