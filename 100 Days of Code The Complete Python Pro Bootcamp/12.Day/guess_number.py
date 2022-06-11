from art import logo
import random
#Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def create_random_number():
    return random.randint(1,100)
correct_number = create_random_number()

print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Psst, the correct number {correct_number}")
options = input("Choose a diffuculty. Type 'easy' or 'hard' ").lower()

if options == 'easy':
    attemps = 10
    print("You have 10 attempts remaining to guess the number")
elif options == 'hard':
    attemps = 5
    print("You have 5 attempts remaining to guest the number")

while attemps > 0:
    guessed = int(input("Make a guess:"))
    if attemps > 1:
        if guessed == correct_number:
            print(f"You got it The answer was {correct_number}")
            attemps = 0
        elif guessed > correct_number:
            print("Too high")
        elif guessed < correct_number:
            print("Too low")
        attemps -= 1
        print("Guess again.")
        print(f"You have {attemps} remaining to guess the number.")   
    elif attemps == 1:
        print("You've run out of guesses,you lose.")
        attemps = 0
    

