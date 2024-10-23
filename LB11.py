import os
import csv
import datetime
import time

class LB11:
    def __init__(self):
        self.DuringFile = None

    def FileOpen(self, file):
        with open(file) as f:
            self.DuringFile = f.readline()

    def FileOpenAll(self, file):
        with open(file) as f:
            self.DuringFile = f.readlines()

    def FilesOpenAllByOne(self, file):
        with open(file) as f:
            self.DuringFile = f.readlines()
            for line in self.DuringFile:
                print(line.strip())

    def FiledUpdate(self, file):
        with open(file, 'a+') as f:
            f.write(f"\n{input()}")

    def FileReWrite(self, file):
        with open(file, 'w') as check:
            for n in range(0, 10):
                check.write(f"{n}\n")

    def print_docs(self, directory):
        all_files = os.walk(directory)
        for catalog in all_files:
            print(f"Папка {catalog[0]} содержит:")
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-'*40)

    def longest_word(self, file):
        with open(file, encoding='utf-8') as f:
            words = f.read().split()
            max_len = len(max(words, key=len))
            for word in words:
                if len(word) == max_len:
                    answer = word
            if len(answer) == 1:
                return answer[0]
            return answer

    def csv_creator(self):
        with open('row_300.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['№', 'Секунда', 'Микросекунда'])
            for line in range(1, 301):
                writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
                time.sleep(0.01)
def main():
    QUEST = LB11()

    # ЗАДАНИЕ 1
    QUEST.FileOpen('text')
    print("ЗАДАНИЕ 1:", QUEST.DuringFile, sep='\n')

    # ЗАДАНИЕ 2
    QUEST.FileOpenAll('text')
    print("ЗАДАНИЕ 2:", QUEST.DuringFile, sep='\n')

    # ЗАДАНИЕ 3
    QUEST.FileOpen('text')
    print("ЗАДАНИЕ 3:", QUEST.DuringFile.strip(), sep='\n')

    # ЗАДАНИЕ 4
    print("ЗАДАНИЕ 4:")
    QUEST.FilesOpenAllByOne('text')

    # ЗАДАНИЕ 5
    QUEST.FiledUpdate('text')
    print("ЗАДАНИЕ 5:")
    QUEST.FilesOpenAllByOne('text')

    # ЗАДАНИЕ 6
    print("ЗАДАНИЕ 6:")
    QUEST.FilesOpenAllByOne('text')
    QUEST.FileReWrite('text')
    QUEST.FilesOpenAllByOne('text')

    # ЗАДАНИЕ 7
    print("ЗАДАНИЕ 7:")
    QUEST.print_docs('D:\Documents\Old\Documents\METODPARABOL')

    # ЗАДАНИЕ 8
    print("ЗАДАНИЕ 8:", QUEST.longest_word('words'))

    # ЗАДАНИЕ 9
    QUEST.csv_creator()

if __name__ == '__main__':
    main()