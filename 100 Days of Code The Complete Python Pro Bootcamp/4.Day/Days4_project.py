import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
select = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_select = random.randint(0,2)

map = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
print(map[select])
print(f"Computer chose {map[computer_select]}")

if select >2 and select < 0:
    print("You typed an invalid number, you lose!") 
if (select == 0 and computer_select == 2) or (select == 1 and computer_select == 0) or (select == 2 and computer_select == 1) :
    print("You win!")
elif(select == 2 and computer_select == 0) or (select == 0 and computer_select == 1) or (select == 1 and computer_select == 2):
    print("You lose")
