"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def isPrime(arg):
    """check if number is prime"""

    # prime number is greater than 1
    if abs(arg) > 1:
        # special case: number=2
        if abs(arg) == 2:
            return True

        # check that cannot be written as the product of two smaller natural numbers
        for i in range(2, arg):
            if arg % i == 0:
                return False

        return True

    else:
        return False


def findAllFactors(arg):
    """find all the factors of a given number"""
    allFactors = []

    for num in range(1, arg + 1):
        if arg % num == 0:
            allFactors.append(num)

    return allFactors


def findPrimeFactors(arg):
    """find all the prime factors of a number"""
    allFactors = findAllFactors(arg)
    primeFactors = []

    for num in allFactors:
        if isPrime(num):
            primeFactors.append(num)

    return primeFactors


if __name__ == '__main__':
    import time
    start = time.time()
    print(max(findPrimeFactors(600851475143)))
    end = time.time()
    print(f"{end}-{start} seconds")
