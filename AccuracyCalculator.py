"""
Accuracy Calculator
"""
import random

notes_hit =  0 #int(input("notes hit? "))
notes_missed = 0 #int(input("notes missed? "))
total_notes = 100
hit_miss = ["h", "h", "h", "h", "h", "h", "h", "h", "h", "m"]
user = random.choice(hit_miss)
i = 0

while i != 100:
    if user == "h":
        hit_acc = random.randint(1, 100)

        match hit_acc:
            case 1:
                notes_hit += 0.9
                print("0.9")
            case 2:
                notes_hit += 0.75
                print("0.75")
            case 3:
                notes_hit += 0.6
                print("0.6")
            case _:
                notes_hit += 1
                print("1")

        # user = input()
    elif user == "m":
        notes_missed += 1
        print("Miss")
        # user = input()
    else:
        pass
        # user = input()

    notes_hit = round(notes_hit, 2)
    user = random.choice(hit_miss)
    accuracy = round(float((notes_hit)/total_notes) * 100, 2)
    print("Accuracy:", accuracy)
    i += 1

print("Notes Hit: " + str(notes_hit))
print("Notes Missed: " + str(notes_missed))
