inches = float(input("Enter inches: "))

while inches >= 0:
    cm = inches * 2.54
    print(f"{inches} inches is {cm:.2f} cm")
    inches = float(input("Enter inches: "))

print("Program ended.")

