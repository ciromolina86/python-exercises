"""
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import numpy as np


def isMultiple(mul, of):
    return mul % of == 0


def smallestMultipleOfNumbers(start=1, stop=10):
    smallestMultiple = 0
    isMultipleMask = [False for x in range(start, stop + 1)]

    for mul in range(stop, stop ** 10, stop):
        smallestMultiple = mul

        for num in range(start, stop + 1):
            if isMultiple(mul=mul, of=num):
                isMultipleMask[num - 1] = True

        if isMultipleMask == [True for x in range(start, stop + 1)]:
            return smallestMultiple
        else:
            isMultipleMask = [False for x in range(start, stop + 1)]


if __name__ == '__main__':
    import time

    start = time.time()

    print(smallestMultipleOfNumbers(start=1, stop=10))

    end = time.time()
    print(f"{end - start} seconds")
