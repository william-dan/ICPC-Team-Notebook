def prefix_function(s):
    n = len(s)
    p = [0]*n
    for i in range(1, n):
        j = p[i - 1]
        while j and s[i] != s[j]:
            j = p[j - 1]
        if s[i] == s[j]:
            j += 1
        p[i] = j
    return p

def kmp_match(text, pat):
    if not pat:
        return list(range(len(text) + 1))
    s = pat + "#" + text
    p = prefix_function(s)
    res = []
    m = len(pat)
    for i in range(m + 1, len(s)):
        if p[i] == m:
            res.append(i - 2*m)
    return res  # starting indices
