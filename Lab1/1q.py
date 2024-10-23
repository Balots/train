LIST = [1 for x in range(10000)]
for i in range(len(LIST)):
    if i % 13 == 0:
        LIST[i] = 0

temp = 0
for i in range(len(LIST)):
    if LIST[i] == 0:
        temp = 0
    LIST[i] = temp
    temp += 1

temp = 0
for i in range(len(LIST)-1, 0, -1):
    if LIST[i] == 0:
        temp = 0
    LIST[i] = min(LIST[i], temp)
    temp += 1
print(LIST)



