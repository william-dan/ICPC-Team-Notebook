# Assume g is adjacency list: g[u] = [(v, w), ...] for weighted.
def bfs(start, g):
    n = len(g)
    dist = [INF]*n
    dist[start] = 0
    dq = deque([start])
    while dq:
        u = dq.popleft()
        for v in g[u]:
            if dist[v] == INF:
                dist[v] = dist[u] + 1
                dq.append(v)
    return dist

def dfs(u, g, vis):
    vis[u] = True
    for v in g[u]:
        if not vis[v]:
            dfs(v, g, vis)
