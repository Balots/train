import random
l = [x for x in range(1, 10000)]
random.shuffle(l)

l.sort(reverse=True)
print(max(l[1] * l[2] * l[3], l[-1]*l[-2]*l[1], l[-1]*l[-2]*l[-3]))