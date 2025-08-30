import random
number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

while guess != number:
    if guess < number:
        print("Too low.")
    else:
        print("Too high.")
    guess = int(input("Guess again: "))

print("Correct! You guessed it.")
