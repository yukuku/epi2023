import timeit


def bruteforce(a: int) -> int:
    ret = 0
    while a > 0:
        if a & 1:
            ret += 1
        a >>= 1
    return ret


def clear_last_one_bit(a: int) -> int:
    ret = 0
    while a > 0:
        a = a & (a - 1)
        ret += 1
    return ret


PRECOMPUTED = {}


def prepare_precomputed():
    if not len(PRECOMPUTED):
        for i in range(0, 65536):
            PRECOMPUTED[i] = clear_last_one_bit(i)


def use_lookup_table(a: int) -> int:
    prepare_precomputed()
    ret = 0
    ret += PRECOMPUTED[a & 0xffff]
    ret += PRECOMPUTED[(a >> 16) & 0xffff]
    ret += PRECOMPUTED[(a >> 32) & 0xffff]
    ret += PRECOMPUTED[(a >> 48) & 0xffff]
    return ret


f = use_lookup_table
print(f(1))
print(f(15))
print(f(16))
print(f(27))
print(f(281474976710656))
print(f(1769472))
print(f(9223372036854775807))
print(f(1134143995904))


print(timeit.timeit(lambda: use_lookup_table(281474976710656), number=100000))