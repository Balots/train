class LB10:
    def __init__(self):
        self.flag = False

    def transform(self, input):
        new_list = []
        prom_symbol = ''
        for item in input:
            if item != ' ':
                prom_symbol += item
            else:
                new_list.append(prom_symbol)
                prom_symbol = ''
        return new_list, tuple(new_list)

    def cortage_changing(self, cortage, elem):
        new_cortage = []
        for item in cortage:
            if item != elem:
                new_cortage.append(item)
        return tuple(new_cortage)

    def dig_numbers(self, string):
        dig_dic = {}
        for item in string:
            if item not in dig_dic.keys():
                dig_dic[item] = string.count(item)
        return dig_dic

    def members_exit(self, items, id):
        if id in items:
            queue = []
            for item in items:
                if item == id:
                    self.flag = not self.flag
                if self.flag == True:
                    queue.append(item)
                if queue.count(id) == 2:
                    break
            self.flag = False
            return tuple(queue)
        else:
            return tuple()

    def cortage_build(self, list1, num_of_cortage):
        answer = []
        if len(list1) % num_of_cortage == 0:
            cortage = []
            for item in list1:
                cortage.append(item)
                if len(cortage) == num_of_cortage:
                    answer.append(tuple(cortage))
                    cortage.clear()
        else:
            cortage = []
            count = 0
            while count < len(list1):
                cortage.append(list1[count])
                count += 1
                if len(cortage) == num_of_cortage:
                    answer.append(tuple(cortage))
                    cortage.clear()
            else:
                for i in range(num_of_cortage - (len(list1) % num_of_cortage)):
                    cortage.append(list1[-1:])
                answer.append(tuple(cortage))
                cortage.clear()
        return answer



def main():
    QUEST = LB10()

    # ЗАДАНИЕ 1
    # 12 14 15 15 16 17 18 19 2 9 0 9 8 172 128
    a, b = QUEST.transform(input())
    print("ЗАДАНИЕ 1")
    print(a, '\n', b)

    # ЗАДАНИЕ 2
    print("ЗАДАНИЕ 2")
    print(QUEST.cortage_changing((1, 2, 3), 1))
    print(QUEST.cortage_changing((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
    print(QUEST.cortage_changing((2, 4, 6, 6, 4, 2), 9))

    # ЗАДАНИЕ 3
    print("ЗАДАНИЕ 3")
    print(QUEST.dig_numbers("1223334444555556666677771111238888438889999"))

    # ЗАДАНИЕ 4
    print("ЗАДАНИЕ 4")
    print(QUEST.members_exit((1, 2, 3), 8))
    print(QUEST.members_exit((1, 8, 3, 4, 8, 8, 9, 2), 8))
    print(QUEST.members_exit((1, 2, 8, 5, 1, 2, 9), 8))

    # ЗАДАНИЕ 5: СОСТАВИТЬ ИЗ СПИСКА КОРТЕЖИ одинаковой длины
    print("ЗАДАНИЕ 5")
    print(QUEST.cortage_build([12, 14, 15, 15, 16, 17, 18, 19, 2, 9, 0, 9, 8, 172, 128], 2))
    print(QUEST.cortage_build([12, 14, 15, 15, 16, 17, 18, 19, 2, 9, 0, 9, 8, 172, 128], 3))
    print(QUEST.cortage_build([12, 14, 15, 15, 16, 17, 18, 19, 2, 9, 0, 9, 8, 172, 128], 4))


if __name__ == '__main__':
    main()