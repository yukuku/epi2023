"""
A 2D array can be written as a sequence in several orders-the most natural ones being row by-row or colurnn-by-column.
In this problem we explore the problem of writing the 2D array in spiral order.
"""


def number(tot: int, r: int, c: int):
    return r * tot + c + 1


def enter(out: list[int], tot: int, n: int, r: int, c: int) -> None:
    if n == 0: return

    if n == 1:
        c += 1
        out.append(number(tot, r, c))
        return

    for _ in range(n):  # n to right
        c += 1
        out.append(number(tot, r, c))
    for _ in range(n - 1):  # n-1 to down
        r += 1
        out.append(number(tot, r, c))
    for _ in range(n - 1):  # n-1 to left
        c -= 1
        out.append(number(tot, r, c))
    for _ in range(n - 2):  # n-2 to up
        r -= 1
        out.append(number(tot, r, c))

    enter(out, tot, n - 2, r, c)


def spiral(n: int) -> list[int]:
    ret = []
    enter(ret, n, n, 0, -1)
    return ret


print(spiral(3))
print(spiral(4))
print(spiral(5))
