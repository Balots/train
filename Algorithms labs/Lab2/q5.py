sm = 10000
def get_info(name):
    with open(name) as file:
        num = int(file.readline())
        for testN in range(num):
            s = 0
            schedule = list(map(int, file.readline().split(' ')))
            for n in range(1, schedule[0]+1):
                if s >= sm:
                    print('Wrong Answer')
                    break
                s += schedule[n+1] - schedule[n]
            print('Accepted')

get_info('input.txt')
