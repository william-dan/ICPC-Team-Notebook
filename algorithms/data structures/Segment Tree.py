class SegTree:
    # supports any associative op, default: min
    def __init__(self, n, func=min, unit=INF):
        self.N = 1
        while self.N < n:
            self.N <<= 1
        self.f = func
        self.unit = unit
        self.st = [unit] * (2 * self.N)

    def build(self, arr):
        for i, v in enumerate(arr):
            self.st[self.N + i] = v
        for i in range(self.N - 1, 0, -1):
            self.st[i] = self.f(self.st[2 * i], self.st[2 * i + 1])

    def update(self, pos, val):
        i = self.N + pos
        self.st[i] = val
        i >>= 1
        while i:
            self.st[i] = self.f(self.st[2 * i], self.st[2 * i + 1])
            i >>= 1

    def query(self, l, r):
        # [l, r)
        resl = self.unit
        resr = self.unit
        l += self.N
        r += self.N
        while l < r:
            if l & 1:
                resl = self.f(resl, self.st[l])
                l += 1
            if r & 1:
                r -= 1
                resr = self.f(self.st[r], resr)
            l >>= 1
            r >>= 1
        return self.f(resl, resr)
