class LB8:
    def __init__(self):
        self.classdict = {
            101:(1234, True),
            102:(2345, False),
            103:(3456, True),
            104:(4567, True),
            None:(None,False)}
        self.my_dict = {
            'first':'so easy'
        }
    def AcessRoom(self, NumAcess):
        acesses = {True: 'Не занят', False: 'Занят'}
        print(f"Пароль для кабинета {NumAcess} - {self.classdict[NumAcess][0]}. Статус: {acesses[self.classdict[NumAcess][1]]}")

    def DictUpdeter(self, **kwargs):
        for key, item in kwargs.items():
            self.my_dict[key] = item
        return self.my_dict

    def splitter(self, string, listing=False):
        if listing:
            return list(tuple(string))
        return tuple(string)

    def inf_ex(self, name, age, company = 'unnamed'):
        print(f"Имя: {name}, возраст: {age}, работа: {company}")

    def sorting(self, Tuple):
        for elem in Tuple:
            if not isinstance(elem, int):
                return Tuple
        return tuple(sorted(Tuple))

def main():
    QUEST = LB8()

    # ЗАДАНИЕ 1
    QUEST.AcessRoom(103)

    # ЗАДАНИЕ 2
    print(QUEST.DictUpdeter(a1=1, a2=2, a3=4, a4=4, a5=5))

    # ЗАДАНИЕ 3
    print(QUEST.splitter("ЖарболовА.К."))
    print(QUEST.splitter("ЖарболовА.К.", listing=True))

    # ЗАДАНИЕ 4
    QUEST.inf_ex("Григорий", 22)
    QUEST.inf_ex("Георгий", 44, "Yandex")

    # ЗАДАНИЕ 5
    print(QUEST.sorting((2, 3, 5, 6, 1)))
    print(QUEST.sorting((10, 9, 8, 7, 6, 5, 4, 3, 2, 1)))
    print(QUEST.sorting((1, 3, 2, 5.1)))


if __name__ == "__main__":
    main()