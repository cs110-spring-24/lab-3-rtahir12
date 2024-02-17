import random

print("Options: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
run = int(input("Enter the problem you want to run: "))

if run == 1:
    print("Running problem 1")
    for i in range(1, 1001):
        print(i)

elif run == 2:
    print("Running problem 2")
    for i in range(1, 1001, 2):
        print(i)

elif run == 3:
    print("Running problem 3")
    for i in range(3, 1001, 3):
        print(i)

elif run == 4:
    print("Running problem 4")
    for i in range(1, 1001):
        if i % 3 == 0 or i % 5 == 0:
            print(i)

elif run == 5:
    print("Running problem 5")
    number = int(input("Enter a number greater than 200: "))
    while number <= 200:
        number = int(input("Please enter a number greater than 200: "))
    for i in range(1, number + 1):
        if i % 11 == 0 or i % 13 == 0:
            print(i)

elif run == 6:
    print("Running problem 6")
    s = "Hello, World!"
    for letter in s:
        print(letter)

elif run == 7:
    print("Running problem 7")
    user_input = input("Enter a string longer than 10 letters: ")
    while len(user_input) <= 10:
        user_input = input("String must be more than 10 letters long. Please enter again: ")
    for i in range(1, len(user_input), 2):
        print(user_input[i])

elif run == 8:
    print("Running problem 8")
    rolls = [0] * 6
    for _ in range(1000):
        roll = random.randint(1, 6)
        rolls[roll - 1] += 1
    for i, count in enumerate(rolls, 1):
        print(f"{i}: {count}")

elif run == 9:
    print("Running problem 9")
    number = int(input("Enter a number: "))
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(f"{number} is not a prime number.")
        else:
            print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

