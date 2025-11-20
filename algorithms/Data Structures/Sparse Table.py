"""Sparse Table for static range queries with idempotent ops (min/max/gcd).

Usage example:
    >>> st = SparseTable([1,5,2,4,3], func=min)
    >>> st.query(1,4)  # min on [1,4)
    2

Build with `SparseTable(arr, func)`, then query with `query(l,r)`.
"""

class SparseTable:
    # for static array, idempotent op like min/max/gcd
    def __init__(self, arr, func=min):
        self.f = func
        n = len(arr)
        self.log = [0]*(n+1)
        for i in range(2, n+1):
            self.log[i] = self.log[i//2] + 1
        K = self.log[n] + 1
        st = [arr[:]]
        j = 1
        while (1 << j) <= n:
            prev = st[j-1]
            cur = []
            step = 1 << j
            half = step >> 1
            for i in range(0, n - step + 1):
                cur.append(self.f(prev[i], prev[i + half]))
            st.append(cur)
            j += 1
        self.st = st

    def query(self, l, r):
        # [l, r) (like KACTL RMQ)
        length = r - l
        k = self.log[length]
        return self.f(self.st[k][l], self.st[k][r - (1 << k)])
