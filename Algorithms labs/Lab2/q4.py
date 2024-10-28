import random
from string import ascii_lowercase
alp = ascii_lowercase


def qsort(l:list) -> list:
    n = 1
    while n < len(l):
        for i in range(len(l) - n):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
        n += 1
    return l

