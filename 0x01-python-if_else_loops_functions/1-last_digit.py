#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = abs(number) % 10
l_digit_n = l_digit * (-1 if number < 0 else 1)
print(f"Last digit of {number} is {l_digit_n}", end=" ")
if l_digit_n > 5:
    print("and is greater than 5")
elif l_digit_n == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
