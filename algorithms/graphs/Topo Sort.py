def topo_sort(g):
    n = len(g)
    indeg = [0]*n
    for u in range(n):
        for v in g[u]:
            indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order  # len < n if cycle
