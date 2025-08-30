length = int(input("Enter the length of the zander in centimeters: "))
if length < 42:
    difference = 42 - length
    print(f"Release the fish back into the lake! It is {difference} cm below the size limit.")
else:
    print("Good catch! The fish meets the size limit.")
