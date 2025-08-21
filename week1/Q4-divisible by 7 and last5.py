# q4_divisible7_or_last5.py

num = int(input("Enter a number: "))
if num % 7 == 0 or num % 10 == 5:
    print(f"{num} satisfies the condition")
else:
    print(f"{num} does not satisfy the condition")

