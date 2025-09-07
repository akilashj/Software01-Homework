import math

def unit_price(diameter, price):
    radius = diameter / 2 / 100
    area = math.pi * radius ** 2
    return price / area


d1 = float(input("Enter diameter of pizza 1 (cm): "))
p1 = float(input("Enter price of pizza 1 (euro): "))
d2 = float(input("Enter diameter of pizza 2 (cm): "))
p2 = float(input("Enter price of pizza 2 (euro): "))

u1 = unit_price(d1, p1)
u2 = unit_price(d2, p2)

print(f"Pizza 1 unit price: {u1:.2f} €/m²")
print(f"Pizza 2 unit price: {u2:.2f} €/m²")

if u1 < u2:
    print("Pizza 1 gives better value for money.")
elif u2 < u1:
    print("Pizza 2 gives better value for money.")
else:
    print("Both pizzas have the same value for money.")
