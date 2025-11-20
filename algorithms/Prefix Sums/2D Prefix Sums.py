"""2D prefix sums helper for fast submatrix sum queries.

Usage example:
    >>> mat = [[1,2],[3,4]]
    >>> sm = SubMatrix(mat)
    >>> sm.sum(0,0,2,2)
    10

Query uses half-open ranges: `sum(u, l, d, r)` returns sum over rows [u,d) and cols [l,r).
"""

class SubMatrix:
    # prefix sums on matrix, query sum over [u:d) x [l:r)
    def __init__(self, v):
        R, C = len(v), len(v[0])
        p = [[0]*(C+1) for _ in range(R+1)]
        for r in range(R):
            pr = p[r+1]
            for c in range(C):
                pr[c+1] = v[r][c] + p[r][c+1] + p[r+1][c] - p[r][c]
        self.p = p

    def sum(self, u, l, d, r):
        p = self.p
        return p[d][r] - p[d][l] - p[u][r] + p[u][l]
