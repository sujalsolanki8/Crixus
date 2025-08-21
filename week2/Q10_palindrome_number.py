# Q10_palindrome_number.py

A = int(input("Enter a number: "))
rev = 0
n = A
while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10

if A == rev:
    print("Yes")
else:
    print("No")
