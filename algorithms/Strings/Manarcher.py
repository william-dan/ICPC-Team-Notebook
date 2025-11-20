"""Manacher's algorithm to compute palindromic radii (odd/even centers).

Usage example:
    >>> p0, p1 = manacher("abba")
    # p1 contains odd radii, p0 even radii

Returns `(p0, p1)` where `p0[i]` is even-radius at i and `p1[i]` odd-radius.
"""

def manacher(s):
    n = len(s)
    # p[0][i]: even, p[1][i]: odd radii
    p0 = [0]*n  # even
    p1 = [0]*n  # odd

    # odd
    l = r = 0
    for i in range(n):
        k = 1 if i > r else min(p1[l + r - i], r - i + 1)
        while i - k >= 0 and i + k < n and s[i-k] == s[i+k]:
            k += 1
        p1[i] = k
        if i + k - 1 > r:
            l, r = i - k + 1, i + k - 1

    # even
    l = r = 0
    for i in range(n):
        k = 0 if i > r else min(p0[l + r - i + 1], r - i + 1)
        while i - k - 1 >= 0 and i + k < n and s[i-k-1] == s[i+k]:
            k += 1
        p0[i] = k
        if i + k - 1 > r:
            l, r = i - k, i + k - 1

    return p0, p1
