# Discrete ternary search on [lo, hi] for a unimodal function f: int -> value
# Assumes f is FIRST strictly increasing, THEN strictly decreasing (single peak).
# Returns (argmax_x, f(argmax_x)).
def ternary_search_discrete(lo, hi, f):
    while hi - lo > 3:
        m1 = lo + (hi - lo) // 3
        m2 = hi - (hi - lo) // 3
        f1 = f(m1)
        f2 = f(m2)
        if f1 < f2:      # for maximum
            lo = m1 + 1
        else:
            hi = m2 - 1

    # brute-force the tiny remaining range
    best_x = lo
    best_val = f(lo)
    for x in range(lo + 1, hi + 1):
        val = f(x)
        if val > best_val:
            best_val = val
            best_x = x
    return best_x, best_val

# Example usage:
# a is unimodal array, we want index of maximum:
# idx, val = ternary_search_discrete(0, len(a) - 1, lambda i: a[i])


# Continuous ternary search on [lo, hi] for a unimodal f: float -> float.
# Returns (x_opt, f(x_opt)) approximately.
def ternary_search_continuous(lo, hi, f, iterations=80):
    for _ in range(iterations):
        m1 = (2 * lo + hi) / 3.0
        m2 = (lo + 2 * hi) / 3.0
        f1 = f(m1)
        f2 = f(m2)
        if f1 < f2:      # for maximum
            lo = m1
        else:
            hi = m2
    x_opt = (lo + hi) / 2.0
    return x_opt, f(x_opt)

# Example:
# def f(x): return - (x - 3) ** 2 + 5  # maximum at x = 3
# x_opt, y_opt = ternary_search_continuous(0.0, 10.0, f)
