# Q9_sum_digits.py

N = int(input("Enter a number: "))
s = 0
while N > 0:
    d = N % 10
    s = s + d
    N = N // 10
print(s)
