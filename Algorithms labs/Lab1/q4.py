import itertools
n = 8
m = 5


def queens():
    for p in itertools.permutations(range(n), m):
        yield [x for x in enumerate(p)]


for q in queens():
    flag = True
    for a, b in ((x, y) for x in q for y in q if x[0] < y[0]):
        if abs(a[0] - b[0]) == abs(a[1] - b[1]):
            flag = False
            break
        if (abs(a[0] - b[0]) == 2 and abs(a[1] - b[1]) == 1) or (abs(a[1] - b[1]) == 2 and abs(a[0] - b[0]) == 1):
            flag = False
            break
    if flag: print(q)
