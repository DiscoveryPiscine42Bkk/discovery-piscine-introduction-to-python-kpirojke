import math
user_input = input("Give me a number: ")
try:
    number = float(user_input)
    rounded = math.ceil(number)
    print(rounded)
except ValueError:
    print("That is not a valid number.")