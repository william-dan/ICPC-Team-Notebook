##############################
# 4. itertools (combinatorics & sequences)
##############################
import itertools as it

# permutations, combinations, product
for p in it.permutations(arr, r):      # r-length permutations
    ...
for c in it.combinations(arr, r):      # combinations (no repeat)
    ...
for c in it.combinations_with_replacement(arr, r):
    ...
for prod in it.product(A, B, repeat=2):
    ...

# accumulate (prefix sums)
from itertools import accumulate
pref = list(accumulate(a))             # pref[i] = sum(a[:i+1])

# groupby (group consecutive equal keys)
for key, group_iter in it.groupby(sorted_pairs, key=lambda x: x[0]):
    group = list(group_iter)

# infinite iterators
it.count(start=0, step=1)              # 0,1,2,3,...
it.cycle([0, 1])                       # 0,1,0,1,...
it.repeat(x, times)                    # x,x,x,...
