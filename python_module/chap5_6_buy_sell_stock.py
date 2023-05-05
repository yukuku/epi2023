def boo(a: list[int]) -> int:
    max_boo = 0
    bing = 9e9
    for n in a:
        if n < bing:
            bing = n
        cur_boo = n - bing
        if cur_boo > max_boo:
            max_boo = cur_boo
    return max_boo


a1 = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(boo(a1))

a1 = [10, 20, 50]
print(boo(a1))

a1 = [20, 10, 5]
print(boo(a1))

a1 = [5, 7, 9, 7, 5]
print(boo(a1))

a1 = [5, 7, 9, 7, 4, 11]
print(boo(a1))

a1 = [3, 5, 7, 9, 7, 4, 11]
print(boo(a1))
