import math

while True:
    a = float(input("Enter coefficient a (or type '_' to quit): "))
    if a == '_':
        break
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Roots are: {root1} and {root2}")
    else:
        print("No real roots")
