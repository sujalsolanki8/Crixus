# q14_min_of_three.py

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)
