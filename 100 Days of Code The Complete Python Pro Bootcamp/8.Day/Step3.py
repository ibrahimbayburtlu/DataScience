from hashlib import new


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(plain_text,shift_amount,direction):
    casear_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift_amount
            casear_text += alphabet[new_position]
        elif direction == "decode":
            new_position = position - shift_amount
            casear_text += alphabet [new_position]
    if direction == "encode":
        print(f"The encoded text is {casear_text}")
    elif direction == "decode":
        print(f"The decoded text is {casear_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text,shift,direction)