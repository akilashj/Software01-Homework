def gallons_to_litres(gallons):
    return gallons * 3.78541

while True:
    gallons = float(input("Enter gallons: "))
    if gallons < 0:
        break
    print(f"{gallons} gallons = {gallons_to_litres(gallons):.2f} litres")
