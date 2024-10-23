import copy
linked_list = [[-1, 'a', 1], [0, 'b', 2], [1, 'c', 0]]
class LinkedSteward:
    DATA = linked_list
    def __init__(self, DATA):
        self.linked_list = DATA
        self.current_element = None

    def switching(self, mod='f'):
        if self.current_element == None:
            self.current_element = 0
            return self.current_element
        if mod == 'f':
            self.current_element = self.linked_list[self.current_element][2]
            return self.current_element
        elif mod == 'b':
            self.current_element = self.linked_list[self.current_element][0]
            return self.current_element

    def updating(self, new_elem, mod='ex'):
        if mod == 'ex':
            self.linked_list[-1][2] = len(self.linked_list)
            self.linked_list.append([len(self.linked_list) - 1, new_elem, 0])
        if mod == 'de':
            LinkedSteward.DATA[-1][2] = len(LinkedSteward.DATA)
            LinkedSteward.DATA.append([len(LinkedSteward.DATA) - 1, new_elem, 0])
            self.linked_list = LinkedSteward.DATA


a = LinkedSteward(linked_list)
b = LinkedSteward(linked_list)
print(a.switching())
a.updating('d', mod='ex')
print(a.linked_list)
print(b.linked_list)
a.updating('e', mod='de')
print(a.linked_list)
print(b.linked_list)