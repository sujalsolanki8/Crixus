# Q8_count_digits.py

N = int(input("Enter a number: "))
count = 0
while N > 0:
    count = count + 1
    N = N // 10
print(count)
