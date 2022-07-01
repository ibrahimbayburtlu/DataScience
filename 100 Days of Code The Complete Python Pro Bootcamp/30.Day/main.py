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
    print("File was closed")