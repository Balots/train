s = ['ABC', 'DEFG', 'AB', 'ABCAB', 'DEFGA', 'FG', 'ABFG', 'ABCAFG', 'FGFG', 'ABABC']


class Root:
    def __init__(self, elem):
        self.elem = elem
        self.images = [elem*2]

    def get_images(self, *roots):
        self.images += f' {self.elem}'.join(roots).split(' ')


class MashTree:
    def __init__(self):
        self.roots = []

    def get_images(self):
        images = []
        for root in self.roots:
            images += root.images
        return set(images)

tree = MashTree()

for elem in s:
    tree.roots.append(Root(elem))

for root in tree.roots:
    root.get_images(*map(lambda x: x.elem, tree.roots))

print(tree.get_images())

for root in tree.roots:
    for image in root.images:
        if image in s and len(image) > 1:
            print(image)
