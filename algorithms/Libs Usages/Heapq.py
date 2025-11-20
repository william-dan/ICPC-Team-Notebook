##############################
# 2. heapq  (priority queue)
##############################
import heapq

# Min-heap (default)
h = []
heapq.heappush(h, (dist, node))
d, u = heapq.heappop(h)

# Initialize from list
h = [5, 1, 7]
heapq.heapify(h)
heapq.heappush(h, 3)
x = heapq.heappop(h)   # smallest element

# Max-heap trick: store negatives
h = []
heapq.heappush(h, -value)
max_val = -heapq.heappop(h)
