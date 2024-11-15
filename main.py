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
        # User-Input
        password = int(user_input)
        if password < 8:
            print("Enter a correct length(>8) for password.!!")
            user_input = input("Please, Enter your number again: ")

        # For length checking
        elif password >= 8:
            try:
                # For shuffling the strings
                random.shuffle(lower_case)
                random.shuffle(upper_case)
                random.shuffle(digits)
                random.shuffle(special_char)

                # For redusing the length of the string and rounding it off
                p1 = round(password * (30/100))
                p2 = round(password * (20/100))

                # For generation of password (characters, and digits and special symbol)
                result = []

                for x in range(p1):
                    result.append(lower_case[x])
                    result.append(upper_case[x])

                for x in range(p2):
                    result.append(digits[x])
                    result.append(special_char[x])

                # For some final Shuffling
                random.shuffle(result)

                # For joining the result and printing
                password = "".join(result)
                print("A Strong Password suggestion: ", password)

                # For Exiting an Infinite loop
                break

            except Passkey as e:
                print("Try again")

    except Exception as e:
        raise "Compileing error..!!"
