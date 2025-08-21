# Q6_sum_even_numbers.py

A = int(input("Enter a number: "))
s = 0
for i in range(2, A+1, 2):
    s = s + i
print(s)
