##############################
# 1. collections
##############################
from collections import deque, defaultdict, Counter, namedtuple

# deque: queue / stack with O(1) push/pop on both ends
dq = deque()
dq.append(x)       # push right
dq.appendleft(x)   # push left
dq.pop()           # pop right
dq.popleft()       # pop left
dq[0], dq[-1]      # front, back

# defaultdict: auto-create missing keys (e.g. list, int)
g = defaultdict(list)
g[u].append(v)
cnt = defaultdict(int)
cnt[key] += 1      # starts from 0

# Counter: frequency map, multiset operations
c = Counter(a_list)
c[key]             # count
c.most_common(1)   # [(value, freq)]
c1 + c2            # add multisets
c1 & c2            # intersection (min counts)

# namedtuple: lightweight struct-like objects
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
p.x, p.y
