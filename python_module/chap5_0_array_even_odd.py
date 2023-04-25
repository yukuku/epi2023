import timeit
from typing import Union, Dict


def partition(a: list[int]):
    place_ptr = 0

    for even_ptr in range(0, len(a)):
        if a[even_ptr] % 2 == 0:
            a[even_ptr], a[place_ptr] = a[place_ptr], a[even_ptr]
            place_ptr += 1


a1 = list(range(1, 100))
partition(a1)
print(a1)
even_count = sum(1 for x in a1 if x % 2 == 0)
print(even_count)
assert all(a % 2 == 0 for a in a1[:even_count])
assert all(a % 2 == 1 for a in a1[even_count:])
