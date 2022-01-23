"""
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import math
import numpy as np


def isMultiple(mul, of):
    return mul % of == 0


def leastCommonMultiple(start=1, stop=10):
    """
    Get the smallest number that can be divided by each of the numbers from start to stop

                   |a * b|
    lcm(a, b) =  -----------
                  gcd(a, b)
    """
    smallestMultiple = 1

    for i in range(start, stop+1):
        smallestMultiple *= i // math.gcd(i, smallestMultiple)
    return smallestMultiple


if __name__ == '__main__':
    import time

    start = time.time()

    print(leastCommonMultiple(start=1, stop=20))
    print(math.lcm())

    end = time.time()
    print(f"{end - start} seconds")
