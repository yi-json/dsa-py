"""
Given a number n, find the number of prime numbers that are strictly less than n

Hint: Use Sieve of Eratosthenes
    - Any multiple of a prime number is not prime
    - 0 and 1 are not prime numbers
    - 2 and 3 are prime numbers
"""

from math import sqrt
def countPrimes(n: int) -> int:
    if n < 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False            

    for i in range(2, int(sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False

    return sum(is_prime)