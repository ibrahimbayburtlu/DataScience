from art import logo
from os import system
import random 

# Angela Yu give a cards list 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
flag = True

def random_cards():
    user_cards.append( random.choice(cards))
    computer_cards.append( random.choice(cards))
random_cards()
random_cards()
def score_total(cards_score):
    score = sum(cards_score) 
    return score

options = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")
# user_score => score_total(user_cards) / user_cards / computer_cards / computer_score => score_total(computer_cards)
if options == 'y':
    print(logo)
    print(f"Your cards {user_cards},current score:{score_total(user_cards)}")
    print(f"Computer's first card:{computer_cards[0]}")
    while flag :
        options2 = input("Type 'y' to get another card, type 'n' to pass: ")
        if options2 == 'y':
            print(f"Your cards {user_cards},current score:{score_total(user_cards)}")
            print(f"Computer's first card:{computer_cards[0]}")
            random_cards()
            print(f"Your final hand:{user_cards},final score:{score_total(user_cards)}")
            print(f"Computer's final hand:{computer_cards},final score:{score_total(computer_cards)}")
        elif options2 == 'n':
            print(f"Your final hand:{user_cards},final score:{score_total(user_cards)}")
            print(f"Computer's final hand:{computer_cards},final score:{score_total(computer_cards)}")
            if score_total(user_cards) > 21 and score_total(computer_cards) > 21:
                if score_total(user_cards) > score_total(computer_cards):
                    print("Congurations! You Win!")
                else:
                    print("You Lose!")
            elif score_total(user_cards) == score_total(computer_cards):
                    print("Draw :) ")
            elif score_total(user_cards) > 21 and score_total(computer_cards) < 21:
                print("You Lose!")
            elif score_total(user_cards) < 21 and score_total(computer_cards) > 21:
                print("You Win!")
            else:
                if score_total(user_cards) > score_total(computer_cards):
                    print("You Win!")
                else:
                    print("You lose")
            flag = False