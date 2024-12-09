memory1 = None
memory2 = None
memory3 = None
memory4 = None
memory5 = None


class Cash:
    def __init__(self):
        self.memory = globals()
        self.requests = []
        self.requests_rate = {}

    def __get_rate(self):
        for request in self.requests:
            try:
                self.requests_rate[request] += 1
            except KeyError:
                self.requests_rate[request] = 1
        self.requests_rate = dict(sorted(self.requests_rate.items(), key=lambda item: item[1]))

    def __get_drive(self):
        for i in range(1, 6):
            try:
                self.memory[f'memory{i}'] = self.requests_rate[list(self.requests_rate.keys())[i-1]]
            except IndexError:
                break

    def request(self, item):
        for i in range(1, 6):
            if self.memory[f'memory{i}'] == item:
                return 0
        self.requests.append(item)
        self.__get_rate()
        self.__get_drive()
        return 1


req = [3, 1, 4, 1, 5]
server = Cash()
k = 0

for i in range(15):
    k += server.request(req[i % 5])

print(k)