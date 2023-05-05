"""
Same, but always use n-1 instead of n, n-1, n-1, and n-2.
The r and c are modified after the call to `number`.
"""


def number(tot: int, r: int, c: int):
    return r * tot + c + 1


def enter(out: list[int], tot: int, n: int, r: int, c: int) -> None:
    if n == 0: return

    if n == 1:
        out.append(number(tot, r, c))
        return

    for _ in range(n - 1):  # to right
        out.append(number(tot, r, c))
        c += 1
    for _ in range(n - 1):  # to down
        out.append(number(tot, r, c))
        r += 1
    for _ in range(n - 1):  # to left
        out.append(number(tot, r, c))
        c -= 1
    for _ in range(n - 1):  # to up
        out.append(number(tot, r, c))
        r -= 1

    enter(out, tot, n - 2, r + 1, c + 1)  # has to manually move to down-right


def spiral(n: int) -> list[int]:
    ret = []
    enter(ret, n, n, 0, 0)
    return ret


print(spiral(3))
print(spiral(4))
print(spiral(5))
