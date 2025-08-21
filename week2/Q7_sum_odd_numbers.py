# Q7_sum_odd_numbers.py

A = int(input("Enter a number: "))
s = 0
for i in range(1, A+1, 2):
    s = s + i
print(s)
