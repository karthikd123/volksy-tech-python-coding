#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last = number % 10
if number < 0: 
    a = a - 10
if number > 5:
    print('Last digit of {} is {} and is less than 5 and is greater than 5' .format(number, last))
elif a == 0:
    print('Last digit of {} is {} and is less than 5 and is 0' .format(number, last)) 
else number > 0:
    print('Last digit of {} is {} and is less than 5 and is less than 6 and not 0' .format(number, last))
