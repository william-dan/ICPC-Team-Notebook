
"""Breadth-First Search (unweighted distances) and Depth-First Search helpers.

Usage example:
    >>> g = [[1,2],[0,3],[0],[1]]
    >>> bfs(0, g)  # distances from node 0
    [0,1,1,2]

Note: this BFS assumes an unweighted graph (neighbors listed directly).
For weighted graphs use Dijkstra.
"""

from collections import deque

##############################
# Iterative BFS
##############################
def bfs(start, n, adj):
    """
    Iterative BFS from 'start'.
    Returns distance array; -1 means unreachable.
    """
    dist = [-1] * n
    dist[start] = 0
    q = deque([start])

    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

    return dist


##############################
# recursive BFS
##############################
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


##############################
# Iterative DFS using a stack
##############################
def dfs_iter(start, n, adj):
    """
    Iterative DFS from 'start' using an explicit stack.
    Returns visit order (optional; you can instead do some processing).
    """
    visited = [False] * n
    order = []

    stack = [start]
    while stack:
        u = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        order.append(u)

        # For the same order as recursive DFS, push neighbors in reverse
        for v in reversed(adj[u]):
            if not visited[v]:
                stack.append(v)

    return order

##############################
# recursive DFS
##############################
def dfs(u, g, vis):
    vis[u] = True
    for v in g[u]:
        if not vis[v]:
            dfs(v, g, vis)
