from math import fabs

# =========================
#  Determinant (double)
# =========================

def det_double(a):
    """
    Determinant of a square matrix of floats.
    Destroys 'a' in-place (Gaussian elimination with partial pivoting).
    """
    n = len(a)
    res = 1.0
    for i in range(n):
        # find pivot row b
        b = i
        for j in range(i + 1, n):
            if fabs(a[j][i]) > fabs(a[b][i]):
                b = j
        if i != b:
            a[i], a[b] = a[b], a[i]
            res *= -1.0
        res *= a[i][i]
        if res == 0:
            return 0.0
        # eliminate below
        for j in range(i + 1, n):
            v = a[j][i] / a[i][i]
            if v != 0.0:
                for k in range(i + 1, n):
                    a[j][k] -= v * a[i][k]
    return res


# =========================
#  IntDeterminant (modular)
# =========================

MOD_DEFAULT = 12345  # same as in KACTL

def det_int(a, mod=MOD_DEFAULT):
    """
    Determinant of an integer matrix modulo 'mod'.
    Destroys 'a' in-place.
    """
    n = len(a)
    ans = 1 % mod
    for i in range(n):
        for j in range(i + 1, n):
            # gcd-like elimination step
            while a[j][i] % mod != 0:
                # integer division like C++ (floor towards 0)
                t = a[i][i] // a[j][i]
                if t != 0:
                    for k in range(i, n):
                        a[i][k] = (a[i][k] - a[j][k] * t) % mod
                a[i], a[j] = a[j], a[i]
                ans = -ans
        ans = (ans * (a[i][i] % mod)) % mod
        if ans == 0:
            return 0
    return (ans + mod) % mod