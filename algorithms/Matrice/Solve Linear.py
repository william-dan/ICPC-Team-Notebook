# =========================
#  SolveLinear (double)
# =========================

def solve_linear(A, b, eps=1e-12):
    """
    Solve A * x = b (double).
    A: n x m list of lists (will be destroyed).
    b: length-n list (will be destroyed).
    Returns (rank, x), where rank = -1 if no solution.
    If multiple solutions, returns one arbitrary solution.
    """
    n = len(A)
    m = len(A[0]) if n else 0
    rank = 0
    col = list(range(m))  # column permutation

    for i in range(n):
        # find pivot with max abs value in submatrix
        br = bc = i
        bv = 0.0
        for r in range(i, n):
            for c in range(i, m):
                v = fabs(A[r][c])
                if v > bv:
                    bv, br, bc = v, r, c

        if bv <= eps:
            # check for inconsistency
            for j in range(i, n):
                if fabs(b[j]) > eps:
                    return -1, None  # no solution
            break

        # swap rows and columns to put pivot at (i, i) (after col perm)
        A[i], A[br] = A[br], A[i]
        b[i], b[br] = b[br], b[i]
        col[i], col[bc] = col[bc], col[i]
        for j in range(n):
            A[j][i], A[j][bc] = A[j][bc], A[j][i]

        # eliminate below
        pivot_inv = 1.0 / A[i][i]
        for j in range(i + 1, n):
            fac = A[j][i] * pivot_inv
            b[j] -= fac * b[i]
            for k in range(i + 1, m):
                A[j][k] -= fac * A[i][k]

        rank += 1

    # back substitution
    x = [0.0] * m
    for i in reversed(range(rank)):
        b[i] /= A[i][i]
        x[col[i]] = b[i]
        for j in range(i):
            b[j] -= A[j][i] * b[i]

    return rank, x


# =========================
#  SolveLinear2 (uniquely determined values)
# =========================

def solve_linear_unique(A, b, eps=1e-12):
    """
    Variant of solve_linear: only returns values that are uniquely determined.
    Undetermined variables get None.
    A, b are destroyed.
    Returns (rank, x_unique) where x_unique[j] is either a float or None.
    """
    n = len(A)
    m = len(A[0]) if n else 0
    rank = 0
    col = list(range(m))

    # same pivoting as solve_linear, but eliminate against ALL rows
    for i in range(n):
        br = bc = i
        bv = 0.0
        for r in range(i, n):
            for c in range(i, m):
                v = fabs(A[r][c])
                if v > bv:
                    bv, br, bc = v, r, c

        if bv <= eps:
            for j in range(i, n):
                if fabs(b[j]) > eps:
                    return -1, None
            break

        A[i], A[br] = A[br], A[i]
        b[i], b[br] = b[br], b[i]
        col[i], col[bc] = col[bc], col[i]
        for j in range(n):
            A[j][i], A[j][bc] = A[j][bc], A[j][i]

        pivot_inv = 1.0 / A[i][i]
        # eliminate in ALL other rows (j != i)
        for j in range(n):
            if j == i:
                continue
            fac = A[j][i] * pivot_inv
            b[j] -= fac * b[i]
            for k in range(i + 1, m):
                A[j][k] -= fac * A[i][k]

        rank += 1

    # Now A is almost diagonal in pivot columns; detect uniquely determined vars
    x = [None] * m
    for i in range(rank):
        # If any free variable (column >= rank) appears in row i, it's not unique
        if any(fabs(A[i][j]) > eps for j in range(rank, m)):
            continue
        pivot_col = col[i]
        x[pivot_col] = b[i] / A[i][i]

    return rank, x


# =========================
#  SolveLinearBinary (over F2)
# =========================

def _first_set_bit_at_or_after(mask, start, m):
    """Return index of first set bit >= start, or m if none."""
    for i in range(start, m):
        if (mask >> i) & 1:
            return i
    return m

def solve_linear_binary(A, b, m):
    """
    Solve A x = b over F2.
    A: list of ints, each int's bits represent a row of length m (0/1).
    b: list of ints (0 or 1).
    Returns (rank, x_mask) where x_mask is an int with bits of solution.
    Returns (-1, None) if no solution.
    Destroys A and b.
    """
    n = len(A)
    rank = 0
    col = list(range(m))

    i = 0
    while i < n:
        # find row with any nonzero entry among remaining rows
        br = i
        while br < n and A[br] == 0:
            br += 1
        if br == n:
            # no rows with nonzero entries left; check for inconsistency
            for j in range(i, n):
                if b[j] & 1:
                    return -1, None
            break

        # pivot column: first set bit in row br at or after i
        bc = _first_set_bit_at_or_after(A[br], i, m)
        if bc == m:
            # row has no set bit, but row != 0 should not happen here; continue
            i += 1
            continue

        A[i], A[br] = A[br], A[i]
        b[i], b[br] = b[br], b[i]
        col[i], col[bc] = col[bc], col[i]

        # swap bits i and bc in all rows (simulate column permutation)
        for j in range(n):
            bit_i = (A[j] >> i) & 1
            bit_bc = (A[j] >> bc) & 1
            if bit_i != bit_bc:
                A[j] ^= (1 << i)
                A[j] ^= (1 << bc)

        # eliminate below
        for j in range(i + 1, n):
            if ((A[j] >> i) & 1) == 1:
                b[j] ^= b[i]
                A[j] ^= A[i]

        rank += 1
        i += 1

    # back-substitution
    x_mask = 0
    for i in reversed(range(rank)):
        if not (b[i] & 1):
            continue
        pivot_col = col[i]
        x_mask |= (1 << pivot_col)
        # subtract this row from all above (since pivot is 1)
        for j in range(i):
            if ((A[j] >> i) & 1) == 1:
                b[j] ^= 1

    return rank, x_mask