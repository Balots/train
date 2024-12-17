class Graf:
    def __init__(self):
        self.dots = {}

    def add(self, name, chain):
        if name not in self.dots.keys():
            self.dots[name] = Elem(name)
        else:
            self.dots[name].add(chain)

    def get(self, name):
        return self.dots[name]


class Elem:
    def __init__(self, name):
        self.name = name
        self.chain = []
        self.length = {}

    def add(self, *args):
        chain, weight = args
        self.chain.append(chain)
        self.length[chain] = l