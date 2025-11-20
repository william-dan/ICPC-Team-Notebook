"""Kruskal's algorithm to compute Minimum Spanning Tree (MST).

Edges should be a list of `(w, u, v)` tuples. Returns `(total_weight, used_edges)`.

Usage example:
    >>> edges = [(1,0,1),(2,1,2),(3,0,2)]
    >>> kruskal(3, edges)
    (3, [(0, 1, 1), (1, 2, 2)])
"""

def kruskal(n, edges):
    # edges: (w, u, v)
    dsu = DSU(n)
    edges.sort()
    total = 0
    used = []
    for w, u, v in edges:
        if dsu.unite(u, v):
            total += w
            used.append((u, v, w))
    return total, used
