"""Dijkstra's algorithm for single-source shortest paths on non-negative weighted graphs.

Graph representation: `g[u] = [(v, w), ...]`

Usage example:
    >>> g = [[(1,2),(2,5)],[(2,1)],[]]
    >>> dijkstra(0, g)
    [0,2,3]
"""

def dijkstra(start, g):
    n = len(g)
    dist = [INF]*n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
