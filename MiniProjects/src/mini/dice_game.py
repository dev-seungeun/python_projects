import random;

count = 0
person_1 = 0
person_2 = 0


def runDiceGame():
    int(input("Press 1 to start dice game or 0 to exit:\n"))
    person1 = random.randint(1, 6)
    person2 = random.randint(1, 6)
    print("person_1 :", person1)
    print("person_2 :", person2)

    return "person1" if person1 > person2 else "person2"


winner = runDiceGame()
print("winner is", winner)
