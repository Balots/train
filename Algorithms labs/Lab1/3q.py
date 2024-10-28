def plus(a, b):
    return a + b

def minus(a, b):
    return a - b
def chin_chopa():
    voc = {'+':plus, '-':minus}
    MAX = 10
    a = input().zfill(MAX)
    r = input()
    b = input().zfill(MAX)
    res = ''
    m = 0
    for i in range(MAX-1, 0, -1):
        s = voc[r](int(a[i]), int(b[i])) + m
        m = 0
        if s >= 10:
            m = 1
            s = s%10
        if s < 0:
            m = -1
            s += 10
        res += str(s)
    return res[::-1]
print(chin_chopa())