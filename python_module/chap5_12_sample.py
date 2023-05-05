"""
Implement an algorithm that takes as input an array of distinct elements and a size,
and returns a subset of the given size of the array elements. All subsets should be equally likely.
Retum the result in input array itself.
"""
import random


def sample(a: list[int], n: int):
    # take one randomly, swap with the first elem
    # then do it again buy excluding the first elem
    for i in range(n):
        pick_index = random.randint(i, len(a) - 1)
        a[i], a[pick_index] = a[pick_index], a[i]


a1 = list(range(1, 100))
sample(a1, 20)
print(a1)
