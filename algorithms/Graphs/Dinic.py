from collections import deque


class Dinic:
    class Edge:
        __slots__ = ("to", "rev", "cap")

        def __init__(self, to, rev, cap):
            self.to = to
            self.rev = rev
            self.cap = cap

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.g[u].append(self.Edge(v, len(self.g[v]), cap))
        self.g[v].append(self.Edge(u, len(self.g[u]) - 1, 0))

    def max_flow(self, s, t):
        flow = 0
        INF = 10 ** 18
        while True:
            level = [-1] * self.n
            q = deque([s])
            level[s] = 0
            while q:
                u = q.popleft()
                for e in self.g[u]:
                    if e.cap > 0 and level[e.to] < 0:
                        level[e.to] = level[u] + 1
                        q.append(e.to)
            if level[t] < 0:
                break
            it = [0] * self.n

            def dfs(u, f):
                if u == t:
                    return f
                for i in range(it[u], len(self.g[u])):
                    it[u] = i
                    e = self.g[u][i]
                    if e.cap > 0 and level[e.to] == level[u] + 1:
                        pushed = dfs(e.to, min(f, e.cap))
                        if pushed:
                            e.cap -= pushed
                            self.g[e.to][e.rev].cap += pushed
                            return pushed
                return 0

            while True:
                pushed = dfs(s, INF)
                if not pushed:
                    break
                flow += pushed
        return flow
