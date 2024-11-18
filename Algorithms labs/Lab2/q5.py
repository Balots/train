def get_info(name):

    with open(name) as file:
        slots = [0 for x in range(10000)]
        num = int(file.readline())
        for testN in range(num):
            flag = False
            schedule = list(map(int, file.readline().split(' ')))
            for n in range(1, schedule[0]*2, 2):
                for i in range(schedule[n], schedule[n+1]):
                    if not slots[i]:
                        slots[i] = 1
                        flag = True
            if not flag:
                print('Wrong')
            else:
                print('Accepted')

get_info('input.txt')
