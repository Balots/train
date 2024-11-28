class HeapElem:
    def __init__(self, elem, mass: list, i: int):
        self.__root = elem
        self.__index = i
        self.__daughters = None if i in (len(mass), len(mass)-1) else [i*2, i*2 + 1]

    def elem(self):
        return self.__root

    def daughter_left(self):
        return self.__daughters[0]

    def daughter_right(self):
        return self.__daughters[1]

    def index(self):
        return self.__index


class Heap:
    def __init__(self, mass: list):
        self.__mass = mass
        self.__members = {0: 0}
        for i in range(1, len(self.__mass)):
            self.__members[i] = HeapElem(self.__mass[i], self.__mass, i)

    def get_members(self):
        return list(self.__members.values())

    def get_mass(self):
        return self.__mass

    def get_member_list(self):
        return self.__members


def test_heap():
    for member in a.get_members()[1:]:
        assert isinstance(member, HeapElem)
    print("Test completed")


def test_is_a_heap():
    flag = True
    l = len(a.get_mass())
    members = a.get_member_list()
    for i in range(1, l//2):
        if i * 2 + 1 <= l:
            if members[i].elem() < members[i*2 + 1].elem():
                flag = False
                break
        if (not i * 2 + 1 <= l) and i*2 <= l:
            if members[i].elem() < members[i*2].elem():
                flag = False
                break
    if not flag:
        print('Massive is not heap!')
    else:
        print('Test completed!')


def test_daughters():
    for member in a.get_members()[1:-2]:
        if not(type(member.daughter_left()) and member.daughter_right()):
            print(f"{member} does not have enough daughters")
            break
    print("Test completed!")


a = Heap([50, 20, 45, 14, 17, 5, 4, 6, 10])
test_daughters()
test_heap()
test_is_a_heap()







