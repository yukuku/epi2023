import typing


def pow_bf(x: float, y: int):
    sign = -1 if y < 0 else 1
    y = abs(y)
    ret = 1
    for _ in range(y):
        ret *= x
    if sign == -1: ret = 1.0 / ret
    return ret


def pow_recursive(x: float, y: int) -> float:
    sign = -1 if y < 0 else 1
    y = abs(y)
    if y == 0:
        ret = 1
    elif y == 1:
        ret = x
    else:
        first_part = y // 2
        half = pow_recursive(x, first_part)
        ret = half * half
        if first_part * 2 != y:
            ret *= x
    if sign == -1: ret = 1.0 / ret
    return ret


def test(fn: typing.Callable, x: float, y: int):
    correct = pow(x, y)
    trythis = fn(x, y)
    if not (0.99 < trythis / correct < 1.01):
        raise AssertionError(f"{x}^{y} should be {correct}, got {trythis}")


for fn in [pow_bf, pow_recursive]:
    test(fn, 3, 0)
    test(fn, 3, 1)
    test(fn, 3, 2)
    test(fn, 3, -2)
    test(fn, 3.5, 20)
    test(fn, 3.5, -20)
    test(fn, -1.0000001, 2000)
