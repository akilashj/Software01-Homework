import random

count = int(input("How many dice to roll? "))

total = 0
for i in range(count):
    roll = random.randint(1, 6)
    print(f"Dice {i+1}: {roll}")
    total += roll

print(f"The sum of rolls is {total}")
