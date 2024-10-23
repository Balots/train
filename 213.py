def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def sort(lst: list[int]) -> list[int]:
    if len(lst) == 0:
        return list(lst)
    pivot = lst[len(lst) // 2]

    lower = [elem for elem in lst if elem < pivot]
    higher = [elem for elem in lst if elem > pivot]
    return (sort(lower) + [elem for elem in lst if elem == pivot] + sort(higher))


class QuickSort:
    @staticmethod
    def sort_recursive(lst: list[int]) -> None:
        x = sort(lst)
        for i in range(len(lst)):
            lst[i] = x[i]

    @staticmethod
    def sort_iterative(lst: list[int]) -> None:
        stack = []
        stack.append(0)
        stack.append(len(lst) - 1)
        while stack:
            high = stack.pop()
            low = stack.pop()
            if lst:
                pivot_index = partition(lst, low, high)
                if pivot_index - 1 > low:
                    stack.append(low)
                    stack.append(pivot_index - 1)
                if pivot_index + 1 < high:
                    stack.append(pivot_index + 1)
                    stack.append(high)
            else:
                break

a = [7, 1]
QuickSort.sort_recursive(a)
print(a)

a = [7, 1]
QuickSort.sort_iterative(a)
print(a)
