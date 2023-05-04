import random


def partition(a: list[int], lo: int, hi: int) -> (int, int):
    # pivot = a[lo]
    # S1 (lt pivot): lo + 1 .. m
    # S2 (eq pivot): m .. u
    # S3 (ge pivot): u .. k
    # unsorted: k .. hi
    pivot = a[lo]
    m = lo + 1
    u = lo + 1
    for k in range(lo + 1, hi):  # everything after the first is considered unsorted
        v = a[k]
        if v == pivot:
            a[u], a[k] = a[k], a[u]
            u += 1
        elif v < pivot:
            a[u], a[k] = a[k], a[u]
            a[m], a[u] = a[u], a[m]
            m += 1
            u += 1
    k = hi
    a[lo], a[m - 1] = a[m - 1], a[lo]
    return m - 1, u


def qs(a: list[int], lo: int = 0, hi: int = None):
    if hi is None: hi = len(a)
    if hi - lo <= 1: return

    pivot_index_lo, pivot_index_hi = partition(a, lo, hi)
    qs(a, lo, pivot_index_lo)
    qs(a, pivot_index_hi, hi)


ori = list(range(10, 50, 10)) + list(range(10, 50)) + list(range(1, 200))
# ori = [30, 30, 30, 30, 30, 30, 40, 50]
# ori = [30, 40, 20, 20, 30, 40]
a1 = ori[:]
random.shuffle(a1)
print(a1)
qs(a1)
print(a1)
assert a1 == sorted(ori)
