from traceback import FrameSummary

Talents = input("Enter the amount of Talents:")
Pounds = input ("Enter the amount of Pounds:")
Lots = input ("Enter the amount of Lots:")

talents = float(Talents)
pounds = float(Pounds)
lots = float(Lots)

Pounds_in_Talent = 20
Lots_in_Pound = 32
Grams_in_Lot = 13.3

Total_Lots = ((talents * Pounds_in_Talent * Lots_in_Pound) + (pounds * Lots_in_Pound) + lots )
Total_Grams = (Total_Lots * Grams_in_Lot)

Kilograms = int(Total_Grams / 1000)
Grams = (Total_Grams % 1000)

print("\nThe weight in modern units: ")
print(f"{Kilograms} kilograms and {Grams:.2f} grams.")


