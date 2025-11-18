class Fenwick:
    # 0-indexed, supports prefix sums on [0, i)
    def __init__(self, n):
        self.s = [0] * n

    def add(self, pos, delta):
        # a[pos] += delta
        n = len(self.s)
        while pos < n:
            self.s[pos] += delta
            pos |= pos + 1

    def sum(self, pos):
        # sum of [0, pos)
        res = 0
        while pos > 0:
            res += self.s[pos - 1]
            pos &= pos - 1
        return res

    def range_sum(self, l, r):  # [l, r)
        return self.sum(r) - self.sum(l)

    def lower_bound(self, target):
        # min pos s.t. sum[0..pos] >= target, returns n if none
        if target <= 0: return -1
        n = len(self.s)
        pos = 0
        pw = 1 << (n.bit_length())
        while pw:
            nxt = pos + pw
            if nxt <= n and self.s[nxt - 1] < target:
                target -= self.s[nxt - 1]
                pos = nxt
            pw >>= 1
        return pos  # in [0..n]
