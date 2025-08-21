# q15_grade.py

per = int(input("Enter percentage: "))

if per < 25:
    print("D")
elif per >= 25 and per < 45:
    print("C")
elif per >= 45 and per < 65:
    print("B")
elif per >= 65 and per < 85:
    print("A")
else:
    print("A+")

