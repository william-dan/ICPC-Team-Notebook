"""Primality testing (deterministic Miller-Rabin for 64-bit) and Pollard Rho
factorization utilities.

Usage examples:
    >>> is_prime(101)
    True
    >>> factorize(91)
    {7:1,13:1}
"""

import random

def sieve_primes(n):
    """Returns (primes, is_prime[0..n])."""
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            step = i
            start = i * i
            if start > n:
                continue
            for j in range(start, n+1, step):
                is_prime[j] = False
    return primes, is_prime

def _is_prime_small(n):
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n % p == 0:
            return n == p
    return None


def is_prime(n):
    """Deterministic Miller-Rabin for 64-bit integers."""
    sp = _is_prime_small(n)
    if sp is not None:
        return sp
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # bases for deterministic up to 2^64
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        composite = True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                composite = False
                break
        if composite:
            return False
    return True


def pollards_rho(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        c = random.randrange(1, n - 1)
        x = random.randrange(2, n - 1)
        y = x
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math_gcd(abs(x - y), n)
            if d == n:
                break
        if d > 1 and d < n:
            return d


def factorize(n):
    """Return prime factors as a dict {prime: exponent}.
    Uses Pollard Rho + Miller-Rabin.
    """
    if n == 1:
        return {}
    if is_prime(n):
        return {n: 1}
    d = pollards_rho(n)
    while d is None:
        d = pollards_rho(n)
    a = factorize(d)
    b = factorize(n // d)
    for k, v in b.items():
        a[k] = a.get(k, 0) + v
    return a


def math_gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
