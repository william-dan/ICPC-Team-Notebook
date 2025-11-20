# =========================
#  MatrixInverse (double)
# =========================

def mat_inv(A, eps=1e-12):
    """
    In-place inversion of a square matrix A (double).
    On success: A becomes A^{-1}, return rank (= n).
    If singular: returns rank < n and A is undefined for inversion.
    """
    n = len(A)
    col = list(range(n))
    tmp = [[0.0] * n for _ in range(n)]
    for i in range(n):
        tmp[i][i] = 1.0

    for i in range(n):
        # find pivot with max abs(A[j][k]) in submatrix
        r = c = i
        for j in range(i, n):
            for k in range(i, n):
                if fabs(A[j][k]) > fabs(A[r][c]):
                    r, c = j, k
        if fabs(A[r][c]) < eps:
            return i  # rank i < n

        # swap row r <-> i in both A and tmp
        A[i], A[r] = A[r], A[i]
        tmp[i], tmp[r] = tmp[r], tmp[i]

        # swap columns c <-> i in both A and tmp
        for j in range(n):
            A[j][i], A[j][c] = A[j][c], A[j][i]
            tmp[j][i], tmp[j][c] = tmp[j][c], tmp[j][i]
        col[i], col[c] = col[c], col[i]

        v = A[i][i]
        # eliminate below
        for j in range(i + 1, n):
            f = A[j][i] / v
            A[j][i] = 0.0
            for k in range(i + 1, n):
                A[j][k] -= f * A[i][k]
            for k in range(n):
                tmp[j][k] -= f * tmp[i][k]

        # normalize row i
        for j in range(i + 1, n):
            A[i][j] /= v
        for j in range(n):
            tmp[i][j] /= v
        A[i][i] = 1.0

    # eliminate above
    for i in range(n - 1, 0, -1):
        for j in range(i):
            v = A[j][i]
            for k in range(n):
                tmp[j][k] -= v * tmp[i][k]

    # reorder columns back according to col[]
    res = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[col[i]][col[j]] = tmp[i][j]

    # copy back into A
    for i in range(n):
        for j in range(n):
            A[i][j] = res[i][j]

    return n  # full rank