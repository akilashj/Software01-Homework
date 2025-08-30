import random

points = int(input("How many random points to generate: "))

inside_circle = 0

for _ in range(points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y < 1:
        inside_circle += 1

pi_approx = 4 * inside_circle / points
print("Approximate value of pi:", pi_approx)
