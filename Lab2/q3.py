import random

xc = [random.randint(-10000, 10000) for x in range(-10000, 10000)]
yc = [random.randint(-10000, 10000) for y in range(-10000, 10000)]

random.shuffle(xc)
random.shuffle(yc)

coor = [(xc[i], yc[i]) for i in range(20000)]


def get_lines(cor: list) -> dict:
    cor.sort()
    lines = {}
    for line in cor:
        if line[0] not in lines.keys():
            lines[line[0]] = [line[1]]
        else:
            lines[line[0]].append(line[1])
    return lines


def get_range(dot1: tuple, dot2: tuple) -> float:
    return (abs(dot1[0] - dot2[0]) ** 2 + abs(dot1[1] - dot2[1]) ** 2) ** 0.5


def get_perimeter(lines: dict) -> float:
    res = 0
    first_line_contur = ()
    second_line_contur = ()
    for xcor, _ in lines.items():
        first_line_contur = (xcor, _[-1])
        second_line_contur = (xcor, _[0])
        res += get_range(first_line_contur, (xcor, _[-1])) + get_range(second_line_contur, (xcor, _[0]))
        if res == 0:
            res += first_line_contur[1] - second_line_contur[1]
    return res + (first_line_contur[1] - second_line_contur[1])


print(get_perimeter(get_lines(coor)))
