import random
l = [x for x in range(1, 10000)]
random.shuffle(l)
f = 678
i = 0
for x in l:
    if x == f:
        print(i)
        break
    i += 1
