correct_username = "python"
correct_password = "rules"

attempts = 0
while attempts < 5:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        print("Entered username or password is incorrect.")
        attempts = attempts + 1

if attempts == 5:
    print("Access denied.")
