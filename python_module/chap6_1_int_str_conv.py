def int_to_str(n: int) -> str:
    if n == 0: return '0'
    neg = n < 0
    n = -n if neg else n
    ret = ''
    while n > 0:
        ret = chr(n % 10 + 48) + ret
        n //= 10
    if neg: ret = '-' + ret
    return ret


def str_to_int(s: str) -> int:
    neg = False
    ret = 0
    for c in s:
        if c == '-': neg = True
        else:
            ret *= 10
            ret += ord(c) - 48
    if neg: ret = -ret
    return ret


print(int_to_str(0))
print(int_to_str(1))
print(int_to_str(-1))
print(int_to_str(120350))
print(int_to_str(-9990999))

print(str_to_int('0'))
print(str_to_int('1'))
print(str_to_int('-1'))
print(str_to_int('120350'))
print(str_to_int('-9990999'))
