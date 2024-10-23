def RootFinder(x, ceil=0, acc=0.0001):
    if x < 0:
        return ValueError

    lf = 0
    rt = x + 1
    md = 0
    while md * md != x:
        md = (rt + lf) / 2
        if md * md < x:
            lf = md
        else:
            rt = md
        if ceil == False:
            if md * md <= (x + acc) and md * md >= (x - acc):
                break
        else:
            if int(md*md) == x:
                return md
    return md
print(RootFinder(12, ceil=0))

def Sort(x):
    sorted(x)
    answer = []
    mid = len(x)//2
    p1, p2 = x[:mid + 1], x[mid + 1:]
    for x in range(mid + 1):
        try:
            answer += [p1[x], p2[x]]
        except IndexError:
            answer += [p1[x]]
    return answer

print(Sort([1, 2, 3, 4, 5, 6]))


def get_elem_num(x, list):
    try:
        h = 0
        cur_part = list
        while True:
            mid = len(cur_part) // 2
            if x in cur_part[:mid]:
                index = mid - 1
                cur_part = list[:mid]
            else:
                h += mid
                index = h
                cur_part = list[mid:]
            if list[index] == x:
                break
        return index
    except IndexError:
        return None

print(get_elem_num(8, [3, 7, 2, 1, 8, 7, 3]))









