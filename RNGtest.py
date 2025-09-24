"""
RNG test
"""
import random

roll = random.randint(1, 10000)
user = input("Press enter to roll. Type \'h\' for a list of commands ")

while user != "b":
    user = user.lower()
    if user == "h":
        print()
        print("\'r\' for results\n\'b\' to exit")
    if user == "r":
        print()
        print("Results: ")
    if user == "b":
        break

    print()
    print(str(float(roll / 100)))
    print()
    user = input("Press enter to roll. Type \'h\' for a list of commands ")
    roll = random.randint(1, 10000)
