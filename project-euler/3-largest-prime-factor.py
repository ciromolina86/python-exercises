"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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


def findAllFactors(arg):
    """find all the factors of a given number"""
    allFactors = []

    for num in range(1, arg + 1):
        if arg % num == 0:
            allFactors.append(num)

    return allFactors


def getPrimeNumbers(n):
    """generate all primes smaller than or equal to n using Sieve of Eratosthenes"""
    prime = [True for i in range(n + 1)]
    p = 2

    while p * p <= n:
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return [p for p in range(2, n + 1) if prime[p]]


def findPrimeFactors(arg):
    """find all the prime factors of a number
    method: prime factorization by division"""
    primeFactors = []
    quotient = None

    for num in getPrimeNumbers(arg):
        quotient = arg / num

        if isPrime(quotient):
            primeFactors.append(num)
            break
        else:
            if arg % num == 0:
                primeFactors.append(num)
                break

    # print(findPrimeFactors(quotient))

    return primeFactors


if __name__ == '__main__':
    import time

    start = time.time()

    print(findPrimeFactors(13195))  # 600851475143 13195
    # print(getPrimeNumbers(13195))  # 600851475143 13195

    end = time.time()
    print(f"{end - start} seconds")
