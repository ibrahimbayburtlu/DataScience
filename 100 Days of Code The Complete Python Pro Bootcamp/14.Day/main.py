from cmath import log
import random 
from data import data
from art import logo
from art import  vs
from os import system

score = 0
# Create a random selection
def selection():
    selection_number = random.randint(0,len(data))
    return selection_number
def correct_answer_solution():
    if first_answer >= second_answer:
        correct_answer = first_answer
    else:
        correct_answer = second_answer
    return correct_answer
def answer_control(answer,score):
    if  answer == your_answer:
        score +=1
        print(f"You're right! Current Score {score}")
    else:
        print(f"Sorry, that's wrong. Final Score:{score}")


choice = data[selection()]
print(f"{choice['name']},a {choice['description']},from {choice['country']}")
first_answer = choice['follower_count'] 
print(vs)
choice = data[selection()]
print(f"{choice['name']},a {choice['description']},from {choice['country']}")
second_answer = choice['follower_count']
your_answer  = input("Who has more followers? Type 'A' or 'B':")

answer = correct_answer_solution()

if your_answer == 'A': your_answer = first_answer
elif your_answer == 'B': your_answer = second_answer


