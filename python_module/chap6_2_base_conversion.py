def str_to_int(s: str, base: int) -> int:
    cs = '0123456789abcdef'
    ret = 0
    for c in s:
        ret *= base
        ret += cs.index(c)
    return ret


def int_to_str(n: int, base: int) -> str:
    if n == 0: return '0'
    cs = '0123456789abcdef'
    ret = ''
    while n > 0:
        ret += cs[n % base]
        n //= base
    return ret[::-1]


def convert_base(s: str, b1: int, b2: int) -> str:
    return int_to_str(str_to_int(s, b1), b2)


print(str_to_int('1000', 10))
print(str_to_int('100000', 10))
print(str_to_int('11111', 2))

print(int_to_str(65536, 16))
print(int_to_str(65536, 8))
print(int_to_str(65536, 2))
print(int_to_str(615, 13))

print(convert_base('615', 7, 13))
