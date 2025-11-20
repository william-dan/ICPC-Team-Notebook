"""Lowest Common Ancestor (LCA) using binary lifting.

Usage example:
    >>> adj = [[1,2],[0],[0]]
    >>> up, depth = build_lca(adj, 0)
    >>> lca(1,2,up,depth)
    0

Functions: `build_lca(adj, root)` returns `(up, depth)`, then use `lca(u,v,up,depth)`.
"""

def build_lca(adj, root=0):
    n = len(adj)
    LOG = max(1, (n).bit_length())
    up = [[root] * n for _ in range(LOG)]
    depth = [0] * n
    parent = [-1] * n
    parent[root] = root
    stack = [root]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            up[0][v] = u
            stack.append(v)
    up[0][root] = root
    for k in range(1, LOG):
        for v in range(n):
            up[k][v] = up[k - 1][up[k - 1][v]]
    return up, depth

def lca(u, v, up, depth):
    if depth[u] < depth[v]:
        u, v = v, u
    LOG = len(up)
    diff = depth[u] - depth[v]
    for k in range(LOG):
        if (diff >> k) & 1:
            u = up[k][u]
    if u == v:
        return u
    for k in range(LOG - 1, -1, -1):
        if up[k][u] != up[k][v]:
            u = up[k][u]
            v = up[k][v]
    return up[0][u]
