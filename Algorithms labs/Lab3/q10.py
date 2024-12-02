class Border:
    def __init__(self, t, value, state):
        self.type = t
        self.value = value
        self.chain = state


class Line:
    def __init__(self, start, end):
        self.__start = Border('right', start, end)
        self.__end = Border('left', end, start)

    def left(self):
        return self.__start

    def right(self):
        return self.__end


class Massive:
    def __init__(self):
        self.head = {}
        self.tail = {}
        self.mid = 0

    def add_line(self, s: Line):
        self.head[s.left().value] = s.left()
        self.tail[s.right().value] = s.right()

    def compose_massive(self):
        dic = sorted(list(self.head.keys())) + sorted(list(self.tail.keys()))
        self.mid = dic[len(self.head.keys())//2]
        self.head.update(self.tail)
        return dic

    def get(self):
        return self.head


def find(mas, num) -> int:
    mid = len(nums)//2
    if num < mas[mid]:
        k = 0
        for i in range(mid):
            if num < mas[i]:
                break
            k += 1
    elif num > mas[mid]:
        k = 0
        for i in range(mid-1, 0, -1):
            if num > mas[mid+i]:
                break
            k += 1

    else:
        k = mid
    return k

m = Massive()

with open('input.txt') as file:
    for i in range(int(file.readline())):
        m.add_line(Line(*map(int, file.readline().split())))

    nums = m.compose_massive()
    print(nums)
    for i in range(int(file.readline())):
        elem = int(file.readline())
        print(elem, find(nums, elem))







