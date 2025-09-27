names = set()

while True:
    name = input("Enter a name: ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nOK")
print("The names entered:")
for n in names:
    print(n)