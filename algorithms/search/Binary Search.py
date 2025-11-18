import bisect

def bin_search_low(lo, hi, ok):
    # find min x in [lo, hi] with ok(x) True
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid): hi = mid
        else: lo = mid + 1
    return lo

def bin_search_high(lo, hi, ok):
    # find max x in [lo, hi] with ok(x) True
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if ok(mid): lo = mid
        else: hi = mid - 1
    return lo


def lower_bound(a, x):
    return bisect.bisect_left(a, x)

def upper_bound(a, x):
    return bisect.bisect_right(a, x)
