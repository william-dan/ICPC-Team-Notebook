def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return a // gcd(a, b) * b

def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extgcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def modinv(a, m=MOD):
    g, x, _ = extgcd(a, m)
    if g != 1:
        return None
    return x % m

def modpow(a, e, m=MOD):
    r = 1
    a %= m
    while e:
        if e & 1:
            r = r * a % m
        a = a * a % m
        e >>= 1
    return r
