"""Common header and IO helpers used across cheatsheet examples.

Provides `INF`, `MOD`, and simple input helpers:
	- `ints()` -> list of ints from a line
	- `int1()` -> single int
	- `strs()` -> list of strings

Usage:
		>>> # import these helpers in your scripts
		>>> # from Header and IO import ints, INF
"""

import sys, math, random, bisect, heapq
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


INF = 10**18
MOD = 10**9 + 7  # or 998244353

# Read helpers
def ints(): return list(map(int, input().split()))
def int1(): return int(input())
def strs(): return input().strip().split()
