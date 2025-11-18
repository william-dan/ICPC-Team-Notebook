def scc(graph):
    n = len(graph)
    rg = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            rg[v].append(u)

    vis = [False]*n
    order = []

    def dfs1(u):
        vis[u] = True
        for v in graph[u]:
            if not vis[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not vis[i]:
            dfs1(i)

    comp = [-1]*n
    cid = 0

    def dfs2(u, cid):
        comp[u] = cid
        for v in rg[u]:
            if comp[v] == -1:
                dfs2(v, cid)

    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1

    return comp, cid  # comp[i] in [0..cid-1]
