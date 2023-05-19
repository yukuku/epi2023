"""
Consider the following two rules that are to be applied to an array of characters.
* Replace each 'a' by two 'd's.
* Delete each entry containing a 'b'.

For example, applying these rules to the array
(a,c,d,b,b,c,a)
results in the array
(d,d,c,d,c,d,d).

Write a program which takes as input an array of characters, and removes each 'b' and replaces each 'a' by two 'd's.
Specifically, along with the array, you are provided an integer-valued size.
Size denotes the number of entries of the array that the operation is to be applied to.
You do not have to worry about preserving subsequent entries.
For example, if the array is (a,b,a,c,_) and the size is 4, then you return (d,d,d,d,c).
You can assume there is enough space in the array to hold the final result.
"""


# Try remove first, decrementing the int given
# the int will become the shift value for the expansion.
def remove_and_expand(A: list[str], size: int) -> list[str]:
    put_at = 0
    scan_at = 0
    while scan_at < size:
        if A[scan_at] != 'b':
            A[put_at] = A[scan_at]
            put_at += 1
        scan_at += 1

    print(A)
    print(put_at)

    shift = sum(c == 'a' for c in A[:put_at])
    scan_at = put_at - 1
    put_at += shift - 1
    print(f'scan_at={scan_at} put_at={put_at}')
    while scan_at >= 0:
        if A[scan_at] == 'a':
            A[put_at] = 'd'
            put_at -= 1
            A[put_at] = 'd'
            put_at -= 1
        else:
            A[put_at] = A[scan_at]
            put_at -= 1
        scan_at -= 1

    return A


s = [c for c in 'abac_']
print(''.join(remove_and_expand(s, 4)))
