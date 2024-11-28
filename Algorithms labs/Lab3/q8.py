com1 = False
com2 = False
com3 = False
syn = False
k1 = 0
k2 = 0
k3 = 0

def comment_unis(text):
    i = 0
    j = -1
    for x in range(len(text)):
        if not i and text[x] == "'":
            i = x
            continue
        if i and text[x] == "'":
            j = x
            break
    return text[:i] + text[j+1:]


while True:
    text = comment_unis(input())

    if '(*' in text:
        com1 = (True, False)[com2 and com3]
    if '{' in text:
        com2 = (True, False)[com1 and com3]
    if '//' in text:
        com3 = (True, False)[com1 and com2]

    if '*)' in text:
        k1 += com1
        com1 = False
    if '}' in text:
        k2 += com2
        com2 = False
    if com3:
        k3 += com3
        com3 = False
    print(k1, k2, k3)
    if not text:
        break

print(k1, k2, k3)

