##############################
# 3. bisect  (binary search on sorted lists)
##############################
import bisect

a = [1, 2, 4, 4, 5]

i = bisect.bisect_left(a, x)   # first index >= x
j = bisect.bisect_right(a, x)  # first index > x
# or:
i = bisect.bisect(a, x)        # alias of bisect_right

# Insert while keeping sorted
bisect.insort_left(a, x)
bisect.insort_right(a, x)

# Typical pattern: check existence / counts
exists = (i < len(a) and a[i] == x)
count_x = bisect.bisect_right(a, x) - bisect.bisect_left(a, x)
