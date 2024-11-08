lt = [x for x in range(1, 10000)]
#lt = lt[9500:10000] + lt[:9500]
lt = lt[500:] + lt[:500]
print(lt)

def binary_search(nums, target, start, end) -> int:
    if start >= end:
        if nums[end] == target:
            return start
        return -1
    mid = (start + end) // 2
    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        return binary_search(nums, target, start, mid - 1)
    else:
        return binary_search(nums, target, mid + 1, end)

def find_disinc(mas: list, elem):
    n0 = 0
    nn = len(mas) - 1
    nm = nn//2
    while (mas[n0] > mas[nn]):
        nm = (nn + n0) // 2
        print(n0, nm, nn)
        if elem == mas[n0]:
            return n0
        elif elem > mas[n0]:
            if elem == mas[nm]:
                return nm
            elif elem > mas[nm]:
                n0 += (nm-n0)
            else:
                nn -= (nn-nm)
        elif elem < mas[nn]:
            if elem == mas[nm]:
                return nm
            else:
                n0 += nm - n0
        else:
            if elem == mas[nm]:
                return nm
            elif elem < mas[nm]:
                nn -= nn - nm
            else:
                n0 += nm - n0
    else:
        return binary_search(mas, elem, n0, nn)
