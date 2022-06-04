#Write your code below this row 👇

for item in range(1,101):
    if item % 3 == 0 and item % 5 != 0:
        print("Fizz")
    elif item % 3 != 0 and item % 5 == 0:
        print("Buzz")
    elif item %3 == 0 and item % 5 == 0:
        print("FizzBuzz")
    else:
        print(item)