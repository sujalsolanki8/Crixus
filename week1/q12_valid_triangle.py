# q12_valid_triangle.py

a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c == 180:
    print("Valid triangle")
else:
    print("Not a valid triangle")
