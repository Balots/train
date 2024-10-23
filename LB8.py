class LB8:
    def __init__(self):
        self.work_days = {'Gregor':[1, 2, 3, 4, 7, 8, 9, 10, 13, 14, 15, 16],
             'Vasiliy':[3, 4, 5, 6, 9, 10, 11, 12, 15, 16, 17, 18],
             'Nikola':[1, 2, 5, 6, 9, 10, 13, 14, 17, 18]}
        self.id_members = {1: 'Gregor', 2:'Vasiliy', 3:'Nikola'}
        self.members_check = {1:[], 2:[], 3:[]}
        self.number_of_s = {}
        self.check = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365,

                 1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666,

                 5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928,

                 5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987,

                 3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]
        self.rating = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
        self.triangles = {1:[12, 25, 3, 48, 71],2:[5, 18, 40, 62, 98],3:[4, 21, 37, 56, 84]}
    def is_member_on_working(self, date):
        print(f"{date} числа на смене были:")
        for id_member, name in self.id_members.items():
            self.number_of_s[name] = len(self.work_days[name])
            if date in self.work_days[self.id_members[id_member]]:
                print(name)

    def results(self):
        self.rating.sort()
        print(f"Три лучших результата {self.rating[:3]}")
        print(f"Три худших результата {self.rating[-3:]}")
        print(f"Все результаты выше 10:")
        for item in self.rating:
            if item > 10:
                print(item)

    def is_triangle_possible(self, *args):
        flag = True
        sides = []
        for item in args:
            sides.append(item)
        for item in sides:
            sides.remove(item)
            if item > sum(sides):
                flag = False
            sides.append(item)
        return flag

    def triangle_square(self, a, b, c):
        return 0.25*(4* a**2 * b**2 - (a**2 + b**2 - c**2)**2)**(0.5)

    def removing(self, list1):
        for item in list1:
            if item == 2:
                list1.remove(item)
        answer = list(map(lambda x: x if x!=3 else 4, list1))
        return answer

    def stack_numbers(self, list1):
        answer_list = []
        for item in list1:
            answer_list.append(item)
            if list1.count(item) > 1:
                s = str(item) * list1.count(item)
                answer_list.append(s)
        return answer_list

def main():
    QUEST = LB8()

    # ЗАДАНИЕ 1
    for day in range(1, 19):
        QUEST.is_member_on_working(day)
    print("Самое большое количество смен:\n", max(QUEST.number_of_s, key=QUEST.number_of_s.get))
    print("Количество чеков:\n", len(QUEST.check))

    # ЗАДАНИЕ 2
    QUEST.results()

    # ЗАДАНИЕ 3
    if QUEST.is_triangle_possible(max(QUEST.triangles[1]), max(QUEST.triangles[2]), max(QUEST.triangles[3])) == True:
        print('Площадь треугольника 1:', QUEST.triangle_square(max(QUEST.triangles[1]), max(QUEST.triangles[2]), max(QUEST.triangles[3])))
    if QUEST.is_triangle_possible(min(QUEST.triangles[1]), min(QUEST.triangles[2]), min(QUEST.triangles[3])) == True:
        print('Площадь треугольника 2:', QUEST.triangle_square(min(QUEST.triangles[1]), min(QUEST.triangles[2]), min(QUEST.triangles[3])))

    # ЗАДАНИЕ 4
    print(QUEST.removing([2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]))
    print(QUEST.removing([4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]))
    print(QUEST.removing([5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]))

    # ЗАДАНИЕ 5
    print(QUEST.stack_numbers([1, 1, 3, 3, 1]))
    print(QUEST.stack_numbers([5, 5, 5, 5, 5, 5, 5]))
    print(QUEST.stack_numbers([2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]))
if __name__ == "__main__":
    main()
