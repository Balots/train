class Deque:
    __LOGGING = 0

    def __init__(self, *elements):
        if not self.__LOGGING:
            self.__head = [elements[0]]
            self.__tail = [elements[-1]]
            self.__inter = [elements[i] for i in range(1, len(elements) - 1)]
            self.__LOGGING = 1
        self.__deque = self.__head + self.__inter + self.__tail

    def push_front(self, elem):
        self.__head = [elem]
        self.__deque = self.__head + self.__deque

    def push_back(self, elem):
        self.__tail = [elem]
        self.__deque = self.__deque + self.__tail

    def pop_front(self):
        self.__head = []
        self.__init__()
        self.__head = [self.__deque[0]]

    def pop_back(self):
        self.__tail = []
        self.__init__()
        self.__tail = [self.__deque[-1]]

    def show(self):
        print(self.__deque)

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