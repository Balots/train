import csv
class LB11:
    def __init__(self):
        self.expenses_file = open('expenses.csv', 'a', encoding='utf-8')
        self.writer = csv.writer(self.expenses_file)
        self.writer.writerow(['Дата', 'Расходы'])
        self.censured_words = ['hello', 'email', 'python', 'the', 'exam', 'wor', 'is']

    def words_numbers(self, file):
        all_words = {}
        count = 0
        with open(file, encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                words = line.split()
                for word in words:
                    count += 1
                    if word not in all_words:
                        all_words[word] = 1
                    else:
                        all_words[word] += 1
        most_freq = max(all_words.values())
        answer = [key for key in all_words if all_words[key] == most_freq]
        return count, answer

    def expenses(self, info):
        self.writer.writerow([info[0], info[1]])

    def stat_file(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            count_letters = 0
            count_words = 0
            for line in lines:
                words = line.split()
                count_words += len(words)
                for word in words:
                    word = word.replace('.', '')
                    count_letters += len(word)
            return count_letters, count_words, len(lines)

    def censure(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read().split()
            for i in range(len(text)):
                if text[i].lower() in self.censured_words:
                    text[i] = '*' * len(text[i])
            return text

    def last_quest(self, file):
        letters = []
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            for letter in text:
                if letter not in letters:
                    letters.append((letter, text.count(letter)))
            return letters
def main():
    QUEST = LB11()

    # ЗАДАНИЕ 1
    count, word = QUEST.words_numbers('Python')
    file = open('Python', encoding='utf-8')
    text = file.read()
    print(f"Задание 1:\n {text}\n\n В тексте всего {count} слов, слово {word} всетречается чаще других.")
    file.close()

    # ЗАДАНИЕ 2
    expenses = {'15.12':1000, '16.12':1500, '17.12':2800, '18.12':450, '19.12':125, '20.12':18000}
    for date, expens in expenses.items():
        QUEST.expenses([date, expens])
    QUEST.expenses_file.close()
    file = open('expenses.csv', 'r', encoding='utf-8')
    smeta = file.read()
    print(f"Задание 2: {smeta}")
    QUEST.expenses_file.close()

    # ЗАДАНИЕ 3
    letters, words, lines = QUEST.stat_file('input.txt')
    print(f"Задание 3: {letters} букв, {words} слов, {lines} строк")

    # ЗАДАНИЕ 4
    file = open('input2.txt', 'r', encoding='utf-8')
    text = file.read()
    print("Задание 4:", f"Изначальный текст: \n {text}", "\nНовый текст:")
    new_text = QUEST.censure('input2.txt')
    for i in range(len(new_text)):
        print(new_text[i], end=' ')

    # ЗАДАНИЕ 5. Сколько раз каждый символ повторяется в тексте?
    print('\nЗадание 5: ', QUEST.last_quest('Python'))


if __name__ == '__main__':
    main()
