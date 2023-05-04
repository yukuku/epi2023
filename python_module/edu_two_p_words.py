# https://www.educative.io/courses/grokking-coding-interview-patterns-python/YQOnN622WRO
#
def reverse_words(s):
    s = list(s)
    lef = 0
    rig = 0

    def rev():
        a = lef
        b = rig - 1
        while a < b:
            s[a], s[b] = s[b], s[a]
            a += 1
            b -= 1

    while True:
        # find right word boundary
        while True:
            if rig >= len(s) or s[rig] == ' ':
                rev()
                break
            rig += 1
        lef = rig
        # find next non-space
        while True:
            lef += 1
            if lef > len(s) or s[lef] != ' ':
                break

        rig = lef
        if lef >= len(s):
            break

    # rev entire str
    lef = 0
    rig = len(s)
    rev()

    return ''.join(s)


reverse_words("Hello     World")
