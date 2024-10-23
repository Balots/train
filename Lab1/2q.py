from random import randint


def Qsort(l:list):
    n = 1
    while n < len(l):
        for i in range(len(l) - n):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
        n += 1
    return l

data = Qsort([int(x) for x in (" ".join([str(randint(1, 200)) for x in range(randint(1, 100))]) + ' 0 '
        + " ".join([str(randint(1, 200)) for x in range(randint(1, 100))]) + ' 0').split(' ')])

l = Qsort([int(x) for x in '1 2 6 8 7 3 0 4 1 6 2 3 9 0'.split(' ')])
print([int(data[i]) for i in range(0, len(data) - 1, 2) if (data[i] != data[i+1] and data[i] != data[i - 1])] + ([data[-1]] if data[-1] != data[-2] else []))
print([l[i] for i in range(len(l) - 1) if l[i] != l[i+1] and l[i] != l[i - 1]] + ([l[-1]] if l[-1] != l[-2] else []))