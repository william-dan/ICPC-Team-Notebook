"""Topological sort for a DAG. Returns a topological ordering of nodes.

Usage example:
    >>> g = [[1],[2],[]]
    >>> topo_sort(g)
    [0,1,2]

If a cycle exists the returned list will have length < n.
"""

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
