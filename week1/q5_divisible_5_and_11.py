# q5_divisible_5_and_11.py

A = int(input("Enter a number: "))
if A % 5 == 0 and A % 11 == 0:
    print(f"{A} is divisible by both 5 and 11")
else:
    print(f"{A} is not divisible by both 5 and 11")
