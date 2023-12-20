s = "abcXYZdef"


def fun(start, stop):
    del s[start: stop]


fun(3, 6)

print(s)
