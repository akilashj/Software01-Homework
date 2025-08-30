numbers = []

number = input("Enter a number: ")

while number != "":
    numbers += [float(number)]
    number = input("Enter a number: ")

if numbers:

    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers were entered.")
