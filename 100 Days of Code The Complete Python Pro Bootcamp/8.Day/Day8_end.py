#Simple Function
def greet():
  print("Hello Angela")
  print("How do you do Jack Bauer?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_name("Jack Baurer")

#Functions with more than 1 input
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
# positional arguments
greet_with("ibrahim","Turkey")

# keyword arguments
greet_with(location="Nowhere",name="Jack Baurer")