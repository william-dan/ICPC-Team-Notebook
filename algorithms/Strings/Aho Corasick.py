from collections import deque


"""Aho–Corasick automaton for multi-pattern string matching.

Usage example:
    >>> ac = AhoCorasick()
    >>> ac.add("he", 0)
    >>> ac.add("she", 1)
    >>> ac.build()
    >>> ac.search("she")
    [(1, 0), (2, 1)]

`add(pattern, index)`, `build()`, then `search(text)` returning list of (pos, pat_idx).
"""

class AhoCorasick:
    def __init__(self):
        self.next = [{}]
        self.link = [0]
        self.out = [[]]

    def add(self, s, idx):
        v = 0
        for ch in s:
            if ch not in self.next[v]:
                self.next[v][ch] = len(self.next)
                self.next.append({})
                self.link.append(0)
                self.out.append([])
            v = self.next[v][ch]
        self.out[v].append(idx)

    def build(self):
        q = deque()
        for ch, v in self.next[0].items():
            q.append(v)
            self.link[v] = 0
        while q:
            v = q.popleft()
            for ch, u in self.next[v].items():
                q.append(u)
                j = self.link[v]
                while j and ch not in self.next[j]:
                    j = self.link[j]
                self.link[u] = self.next[j].get(ch, 0)
                self.out[u] += self.out[self.link[u]]

    def search(self, text):
        v = 0
        res = []  # list of (pos, pattern_index)
        for i, ch in enumerate(text):
            while v and ch not in self.next[v]:
                v = self.link[v]
            v = self.next[v].get(ch, 0)
            for pat in self.out[v]:
                res.append((i, pat))
        return res
