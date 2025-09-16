import random
range = int(input("What range do you want to guess100 from? "))
num = random.randint(1, range)
correct = False
numOfGuess = 0
guess = 0
while correct == False:
    guess = int(input("What is your guess "))
    numOfGuess = numOfGuess + 1
    if guess == num:
        print("Thats correct!")
        print(f"You took {numOfGuess} trys to guess!")
        correct = True
    elif guess > num:
        print(f"{guess} is too big!")
    else:
        print(f"{guess} is too small!")