from PIL import Image
import pytesseract

class DoWork:
    def __init__(self, file: str, lang='rus+eng', path='pic/'):
        self.lang = lang
        self.path = path
        self.file = file

    def its(self):
        return pytesseract.image_to_string(Image.open(self.path + self.file), self.lang)


a = DoWork('CODE1.PNG', lang='eng+rus')
print(a.its())