##############################
# 6. functools (lru_cache, reduce)
##############################
from functools import lru_cache, reduce

# Memoized recursion (DP)
@lru_cache(maxsize=None)
def f(i, j):
    ...
    return ans

# reduce: fold (e.g. xor of list)
import operator as op
from functools import reduce
xor_all = reduce(op.xor, arr, 0)
