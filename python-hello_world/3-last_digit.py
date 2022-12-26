#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
if number < 0:
    n = n - 10
if n > 5:
    print('Last digit of {} is {} and is less than 5 and is greater than 5' .format(number, last));
elif n == 0:
    print('Last digit of {} is {} and is less than 5 and is 0' .format(number, last)); 
else:
    print('Last digit of {} is {} and is less than 5 and is less than 6 and not 0' .format(number, last));
