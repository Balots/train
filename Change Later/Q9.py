from itertools import product
from string import ascii_uppercase

alp = ascii_uppercase[:25]
W = product(alp, repeat = 8)
file = open('var.txt', 'w')
for l in W:
    cur = ''.join(l)
    file.write(cur)
    print(cur)