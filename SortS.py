def merge(a, b):
    r = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            r.append(a[i])
            i += 1
        else:
            r.append(b[j])
            j += 1

    r += a[i:] + b[j:]
    return r

def sort_list(arr:list) -> list:
    centre = len(arr)//2
    a = arr[:centre]
    b = arr[centre:]
    if len(a) > 1:
        a = sort_list(a)
    if len(b) > 1:
        b = sort_list(b)

    return merge(a, b)

arr = [45, 3, 2, 23, 4, 12, 4, 54,5, 757]
arr = sort_list(arr)
print(arr)

def b_find(arr:list, elem:int) -> int:
    centre = len(arr)//2
    if arr[centre] == elem:
        return centre
    elif arr[centre] > elem:
        return b_find(arr[:centre], elem)
    else:
        return b_find(arr[centre:], elem) + len(arr[:centre])
print(b_find(arr, 23))


