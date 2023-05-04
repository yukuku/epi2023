import random


def partition(a: list[int], lo: int, hi: int) -> int:
    # pivot = a[lo]
    # S1 (lower than pivot): lo + 1 .. m
    # S2 (ge than pivot): m .. k
    # unsorted: k .. hi
    pivot = a[lo]
    m = lo + 1
    for k in range(lo + 1, hi):  # everything after the first is considered unsorted
        v = a[k]
        if v < pivot:
            a[m], a[k] = a[k], a[m]
            m += 1
    a[lo], a[m - 1] = a[m - 1], a[lo]
    return m - 1


def qs(a: list[int], lo: int = 0, hi: int = None):
    if hi is None: hi = len(a)
    if hi - lo <= 1: return

    # implemented using https://visualgo.net/en/sorting?slide=12
    pivot_index = partition(a, lo, hi)
    qs(a, lo, pivot_index)
    qs(a, pivot_index + 1, hi)


a1 = list(range(1, 100))
random.shuffle(a1)
print(a1)
qs(a1)
print(a1)
assert a1 == list(range(1, 100))
