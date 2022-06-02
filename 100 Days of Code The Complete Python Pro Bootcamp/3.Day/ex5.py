# 🚨 Don't change the code below 👇
import socketserver


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

total1 = 0
total2 = 0

total1 += lower_case_name1.count('t')
total1 += lower_case_name1.count('r')
total1 += lower_case_name1.count('u')
total1 += lower_case_name1.count('e')

total2 += lower_case_name1.count('l')
total2 += lower_case_name1.count('o')
total2 += lower_case_name1.count('v')
total2 += lower_case_name1.count('e')

total1 += lower_case_name2.count('t')
total1 += lower_case_name2.count('r')
total1 += lower_case_name2.count('u')
total1 += lower_case_name2.count('e')

total2 += lower_case_name2.count('l')
total2 += lower_case_name2.count('o')
total2 += lower_case_name2.count('v')
total2 += lower_case_name2.count('e')

score = total1 * 10 + total2


if(score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score > 40 and score < 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")