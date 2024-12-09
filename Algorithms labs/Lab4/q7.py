class Tree:
    def __init__(self, mas: list, ):
        self.prev = mas
        self.mas = [0] + mas
        self.numbers = dict((self.mas[i], i) for i in range(1, len(self.mas)))

    def restruct(self):
        for i in range(len(self.mas) - 1, 0, -1):
            if self.mas[i] < self.mas[i//2]:
                self.mas[i//2], self.mas[i] = self.mas[i], self.mas[i//2]

        self.numbers = dict((self.mas[i], i) for i in range(1, len(self.mas)))

    def show(self):
        print(self.mas)

    def show_prev(self):
        print(self.prev)

    def __sum(self, a, b):
        return sum(self.prev[a:b+1])

    def __change(self, a, b):
        self.mas[self.numbers[self.prev[a]]] = b
        self.prev[a] = b
        self.restruct()

    def request(self, t, a, b):
        return [self.__sum(a, b), self.__change(a, b)][t == 2]


mas = [1, 7, 15, 8, 9, 15, 15, 19, 5, 19]

t = Tree(mas)
t.restruct()
t.show()
t.request(2, 4, 25)
t.show()
t.show_prev()
print(t.request(1, 1, 8))

