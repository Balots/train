class Base:
    def __init__(self):
        self.dict = {}

    def add(self, *args):
        key, value = args
        self.dict[key] = value

    def delete(self, arg):
        del self.dict[arg]

    def update_key_value(self, *args):
        key, value = args
        self.dict[key] = value

    def print(self, arg):
        print(self.dict[arg])


class Interface:
    def init(self):
        self.base = Base()
        self.input = None
        self.command_dict = {
            'ADD': self.base.add,
            'DELETE': self.base.delete,
            'UPDATE': self.base.update_key_value,
            'PRINT': self.base.print
        }

    def interpretend(self, stroke):
        return stroke.split(' ')

    def get_comand(self, interpret_stroke):
        self.command_dict[interpret_stroke[0]](*interpret_stroke[1:])

    def main_loop(self):
        while True:
            command = input('ббедхре йнллюмдс: ')
            if command:
                self.get_comand(self.interpretend(command))
            else:
                break


Interface().main_loop()