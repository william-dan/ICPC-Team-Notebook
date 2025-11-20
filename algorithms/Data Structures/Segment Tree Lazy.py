"""Segment tree with lazy propagation: range add & range sum (0-indexed).

Usage example:
        >>> st = SegTreeLazy(8)
        >>> st.add(1,4,5)        # add 5 to indices [1,4)
        >>> st.range_sum(0,5)
        15

Methods:
    - `add(L, R, val)`: add `val` to [L, R)
    - `range_sum(L, R)`: return sum over [L, R)
"""

class SegTreeLazy:
    def __init__(self, n):
        self.n = 1
        while self.n < n:
            self.n <<= 1
        self.sum = [0] * (2 * self.n)
        self.lazy = [0] * (2 * self.n)

    def _apply(self, k, l, r, val):
        self.sum[k] += val * (r - l)
        self.lazy[k] += val

    def _push(self, k, l, r):
        if self.lazy[k] != 0 and k < self.n:
            m = (l + r) // 2
            self._apply(k * 2, l, m, self.lazy[k])
            self._apply(k * 2 + 1, m, r, self.lazy[k])
            self.lazy[k] = 0

    def add(self, L, R, val, k=1, l=0, r=None):
        if r is None:
            r = self.n
        if R <= l or r <= L:
            return
        if L <= l and r <= R:
            self._apply(k, l, r, val)
            return
        self._push(k, l, r)
        m = (l + r) // 2
        self.add(L, R, val, k * 2, l, m)
        self.add(L, R, val, k * 2 + 1, m, r)
        self.sum[k] = self.sum[k * 2] + self.sum[k * 2 + 1]

    def range_sum(self, L, R, k=1, l=0, r=None):
        if r is None:
            r = self.n
        if R <= l or r <= L:
            return 0
        if L <= l and r <= R:
            return self.sum[k]
        self._push(k, l, r)
        m = (l + r) // 2
        return self.range_sum(L, R, k * 2, l, m) + self.range_sum(L, R, k * 2 + 1, m, r)
