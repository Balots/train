class Tree:
    def __init__(self, mas: list):
        self.mas = mas
        self.branches = self.restruct(self.mas)
        self.index = self.indexes([i for i in range(len(self.mas))])

    @staticmethod
    def restruct(mas):
        if len(mas) > 1:
            return Tree.restruct(mas[:len(mas)//2]) + Tree.restruct(mas[len(mas)//2:]) + [sum(mas)]
        if len(mas) == 1:
            return []

    @staticmethod
    def indexes(list_of_i):
        if len(list_of_i) > 1:
            return Tree.indexes(list_of_i[:len(list_of_i)//2]) + Tree.indexes(list_of_i[len(list_of_i)//2:]) + [list_of_i]
        if len(list_of_i) == 1:
            return []

    def __get_lines(self, a, b):
        md = len(self.mas)
        i = 0
        sum = 0
        elem = [i for i in range(a, b+1)]
        for i in range(len(self.index)):
            if elem == self.index[i]:
                return self.branches[i]
        if b < md:
            pass
        elif a < md <= b:
            pass
        elif md <= a:
            pass







mas = [1, 7, 15, 8, 9, 15, 15, 19, 5, 19]

print(Tree.restruct(mas))
print(Tree.indexes([i for i in range(len(mas))]))
print(len(Tree.restruct(mas)), len(Tree.indexes([i for i in range(len(mas))])))
