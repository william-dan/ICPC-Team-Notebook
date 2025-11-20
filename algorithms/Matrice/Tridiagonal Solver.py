# =========================
#  Tridiagonal solver
# =========================

def tridiagonal(diag, super_diag, sub_diag, b):
    """
    Solve tridiagonal system with main diagonal 'diag',
    super-diagonal 'super_diag', sub-diagonal 'sub_diag' and RHS b.
    All are lists of floats. Returns x (solution), leaves copies of inputs.
    This matches the KACTL algorithm, including the special stability trick.
    """
    n = len(b)
    diag = diag[:]          # copy, we will modify
    b = b[:]                # copy
    tr = [0] * n            # "swap-trick" flags

    # forward elimination
    i = 0
    while i < n - 1:
        if abs(diag[i]) < 1e-9 * abs(super_diag[i]):  # diag[i] == 0 (numerically)
            b[i + 1] -= b[i] * diag[i + 1] / super_diag[i]
            if i + 2 < n:
                b[i + 2] -= b[i] * sub_diag[i + 1] / super_diag[i]
            diag[i + 1] = sub_diag[i]
            tr[i + 1] = 1
            i += 2  # note the ++i in C++ after setting tr[++i]
        else:
            diag[i + 1] -= super_diag[i] * sub_diag[i] / diag[i]
            b[i + 1] -= b[i] * sub_diag[i] / diag[i]
            i += 1

    # backward substitution
    for i in range(n - 1, -1, -1):
        if tr[i]:
            # swap b[i] and b[i-1]; diag[i-1] = diag[i]; divide by super_diag[i-1]
            b[i], b[i - 1] = b[i - 1], b[i]
            diag[i - 1] = diag[i]
            b[i] /= super_diag[i - 1]
        else:
            b[i] /= diag[i]
            if i > 0:
                b[i - 1] -= b[i] * super_diag[i - 1]

    return b