# FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("Something")
except KeyError as error_messeage:
    print(f"That key {error_messeage} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    #raise TypeError("This is an error that I made up")


height = float(input("Height: "))
weight = int(input("Height: "))

if height > 3:
    raise ValueError("Human height should not be over 3 metres.")



bmi = weight / height ** 2
print(bmi) 