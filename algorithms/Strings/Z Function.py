"""Z-function: for each position i, longest substring starting at i matching prefix.

Usage example:
    >>> z_function("abacaba")
    [0,0,1,0,3,0,1]

Returns list `z` of length n where z[i] is the match length at i.
"""

def z_function(s):
    n = len(s)
    z = [0]*n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z
