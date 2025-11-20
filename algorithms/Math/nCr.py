"""Precompute factorials and inverse factorials to compute nCr modulo MOD.

Usage example:
    >>> nCr(5,2)
    10

Adjust `NMAX` if you need larger precomputation limits.
"""

# Precompute up to N
NMAX = 2 * 10**5
fact = [1] * (NMAX + 1)
invfact = [1] * (NMAX + 1)
for i in range(1, NMAX + 1):
    fact[i] = fact[i - 1] * i % MOD
invfact[NMAX] = modpow(fact[NMAX], MOD - 2)
for i in range(NMAX, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD

def nCr(n, r):
    if r < 0 or r > n: return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD
