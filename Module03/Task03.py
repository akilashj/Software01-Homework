gender = input("Enter your biological gender (Male/Female): ")
hemoglobin = int(input("Enter your hemoglobin value (g/l): "))

if gender == "Female":
    if hemoglobin < 117:
        print("Your hemoglobin value is low.")
    elif hemoglobin <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
elif gender == "Male":
    if hemoglobin < 134:
        print("Your hemoglobin value is low.")
    elif hemoglobin <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
else:
    print("Invalid gender entered.")
