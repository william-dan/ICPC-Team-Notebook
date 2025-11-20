"""Disjoint Set Union (Union-Find) with union by size and path compression.

Usage example:
    >>> dsu = DSU(5)
    >>> dsu.unite(0,1)
    True
    >>> dsu.same(0,2)
    False

This structure supports: find(x), unite(a,b), same(a,b).
"""

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        while x != self.p[x]:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def unite(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return False
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        self.p[b] = a
        self.sz[a] += self.sz[b]
        return True

    def same(self, a, b):
        return self.find(a) == self.find(b)
