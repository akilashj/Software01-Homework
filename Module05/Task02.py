numbers = []

num = input("Enter a number: ")
while num != "":
    numbers += [float(num)]
    num = input("Enter a number: ")

numbers.sort(reverse=True)
print("The five greatest numbers are:")
print(numbers[:5])
