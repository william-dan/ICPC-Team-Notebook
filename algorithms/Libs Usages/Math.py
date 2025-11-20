##############################
# 5. math (number theory / geometry)
##############################
import math

math.gcd(a, b)
math.lcm(a, b)          # Python 3.9+
math.isqrt(n)           # integer sqrt
math.sqrt(x)            # float sqrt
math.factorial(n)
math.comb(n, k)         # n choose k (exact integer)
math.perm(n, k)         # permutations (3.8+)
math.hypot(x, y)        # sqrt(x*x + y*y)
math.pi, math.tau, math.e

# Angle <-> radians
math.radians(deg)
math.degrees(rad)

# Useful for EPS in geometry
EPS = 1e-9
