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
