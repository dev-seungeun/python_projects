import random

number = random.randint(1, 10)
for i in range(0, 3):
    user = int(input("guess the number : "))
    if user == number:
        print("Hurray!!")
        print(f"you guess the number right it's {number}")
        break
    elif user > number:
        print("Your guess is too high\n")
    elif user < number:
        print("Your guess is too low\n")
else:
    print(f"Nice Try!, but the number is {number}")
