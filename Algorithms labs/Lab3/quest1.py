class Deque:
    __LOGGING = 0

    def __init__(self, *elements):
        self.__head = 0
        self.__tail = len(elements)
        self.__deque = [x for x in elements]

    def push_front(self, elem):
        self.__deque = [elem] + self.__deque

    def push_back(self, elem):
        self.__deque = self.__deque + [elem]
        self.__tail += 1

    def pop_front(self):
        self.__head += 1

    def pop_back(self):
        self.__tail -= 1

    def show(self):
        print([self.__deque[i] for i in range(self.__head, self.__tail)])

a = Deque(1, 2, 3, 4, 5)
a.show()
a.pop_back()
a.show()
a.push_back(23)
a.show()
a.pop_front()
a.show()
a.push_front(23)
a.show()