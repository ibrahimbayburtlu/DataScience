#Read this the code in main.py
#Spot the problems 🐞.
#Modify the code to fix the program.
'''
year = input("Which year do you want to check?")
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
    print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
''' 
# not all arguments converted during string formatting
year = int(input("Which year do you want to check?")) 
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
            print("Leap year.")
else:
    print("Not leap year.")
  

