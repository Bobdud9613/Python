"""
RNG test
"""
import random

roll = random.randint(1, 10000)
user = input("Press enter to roll. Type \'h\' for a list of commands ")

while True:
    user = user.lower()

    match user:
        case "h":
            print("\n\'r\' for results\n\'b\' to exit\n")        
        case "r":
            print("\nResults: \n")
        case "b":
            break
        case "":
            print("\n" + str(float(roll / 100)) + "\n")

    user = input("Press enter to roll. Type \'h\' for a list of commands ")
    roll = random.randint(1, 10000)
