#!/usr/bin/python3
import random
number = random.randint(-10, 10)
i = -11
while (i != number):
    i += 1
    if i == number and number > 0:
        print("{} is positive".format(number))
    elif i == number and number == 0:
        print("{} is Zero".format(number))
    elif i == number and number < 0:
        print("{} is negative".format(number))
