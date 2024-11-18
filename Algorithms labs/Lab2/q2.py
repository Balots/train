import random
l = [x for x in range(1, 10000)]
random.shuffle(l)
h1, h2, h3 = 0, 0, 0
l1, l2 = 1000000, 1000000

def maximum(elem):
    global h1, h2, h3
    if h1 < elem:
        if h2 < elem:
            if h3 < elem:
                h1 = h2
                h2 = h3
                h3 = elem
            else:
                h1 = h2
                h2 = elem
        else:
            h1 = elem

def minimum(elem):
    global l1, l2
    if l1 > elem:
        if l2 > elem:
            l1 = l2
            l2 = elem
        else:
             l1 = elem

for elem in l:
    maximum(elem)
    minimum(elem)

print(max(h1 * h2 * h3, l1*l2*h3, l[-1]*l[-2]*l[-3]))