import random
import string

class Passkey(Exception):
    pass

lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
digits = list(string.digits)
special_char = list(string.punctuation)

user_input = input("How many characters do you want in your password? ")

while True:
    try:
        password = int(user_input)
        if password < 8:
            print("Enter a correct length(>8) for password.!!")
            user_input = input("Please, Enter your number again: ")

        elif password >= 8:
            try:
                random.shuffle(lower_case)
                random.shuffle(upper_case)
                random.shuffle(digits)
                random.shuffle(special_char)

            except Passkey as e:
                print("Try again")
