"""
10001st prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def isPrime(arg):
    """check if number is prime"""
    # zero and one are not prime numbers
    if abs(arg) == 0 or abs(arg) == 1:
        return False

    # special case: two
    elif abs(arg) == 2:
        return True

    else:
        for i in range(2, int(arg ** 0.5) + 1):
            if arg % i == 0:
                return False
        return True


def primeNumberGenerator():
    """generate an infinite sequence of prime numbers"""
    number = 2

    while True:
        if isPrime(number):
            yield number
        number += 1


if __name__ == '__main__':
    import time

    start = time.time()

    prime = primeNumberGenerator()
    nth = 100001
    for i in range(1, nth + 1):
        num = next(prime)
        if i == nth:
            print(f'{i}th prime = {num}')

    end = time.time()
    print(f"{end - start} seconds")
