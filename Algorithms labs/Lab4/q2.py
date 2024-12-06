cap = [1, 2, 3, 4, 5]
o = sum(cap)
cap = sorted(cap)


def delimiter(mas):
    n = list(map(lambda cap: cap * 0.01, mas))
    print(mas)
    return sorted([(mas[i] + mas[i - 1] - n[i] - n[i-1]) for i in range(1, len(mas), 2)] + ([mas[-1]] if len(mas) % 2 != 0 else []))


def delimiter2(mas):
    n = list(map(lambda cap: cap * 0.01, mas))
    t = ([mas[-1]], [])[len(mas) % 2 == 0]
    mas = (mas, mas[:-1])[len(mas) % 2 != 0]
    print(mas, t)
    return sorted([(mas[i] + mas[-i - 1] - n[i] - n[-i-1]) for i in range(len(mas)//2)] + t)


while True:
    cap = delimiter2(cap)
    if len(cap) == 1:
        break

print(cap)
print(o - cap[0])
# 1 4 5 7 11
