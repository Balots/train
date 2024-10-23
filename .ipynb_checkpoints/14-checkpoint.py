class LB14:
    def __init__(self, ini):
        self.ini = ini
        self._text = []

    def text_creator(self, text):
        self._text = text

class ReaderText(LB14):
    def __init__(self, file):
        super().__init__(1)
        self.file = file

    def file_reader(self):
        file = open(self.file, 'r', encoding='utf-8')
        text = file.read()
        return text


def main():
    QUEST = [ReaderText('Python'), LB14(1)]
    QUEST[0].text_creator(QUEST[0].file_reader())
    print(QUEST[0]._text)
    print(QUEST[1]._text)
if __name__ == '__main__':
    main()