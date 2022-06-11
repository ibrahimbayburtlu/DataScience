from cmath import log
import random 
from data import data
from art import logo
from art import  vs
from os import system

score = 0
flag = True
# Create a random selection
def selection():
    selection_number = random.randint(0,len(data)-1)
    return selection_number

# Create function about in correct_answer_solution()
def correct_answer_solution():
    if first_answer >= second_answer:
        correct_answer = first_answer
    else:
        correct_answer = second_answer
    return correct_answer

def answer_control(score):
    if  correct_answer_solution() == your_answer:
        score +=1
        print(f"You're right! Current Score {score}")
    else:
        print(f"Sorry, that's wrong. Final Score:{score}")

print(logo)
choice = data[selection()]

while flag:
    # First Person
    print(f"{choice['name']},a {choice['description']},from {choice['country']}")
    first_answer = choice['follower_count'] 
    print(vs)
    # Second Person
    choice = data[selection()]
    print(f"{choice['name']},a {choice['description']},from {choice['country']}")
    second_answer = choice['follower_count']
    your_answer  = input("Who has more followers? Type 'A' or 'B':")
    if your_answer == 'A': your_answer = first_answer
    elif your_answer == 'B': your_answer = second_answer
    if  correct_answer_solution() == your_answer:
        system('cls')
        score +=1
        print(f"You're right! Current Score {score}")
    else:
        print(f"Sorry, that's wrong. Final Score:{score}")
        flag = False



