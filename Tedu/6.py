import heapq


class Heap:
    def __init__(self, n: int):
        self.heap = list()
        self.n = n
        self.arr = None

    def pull(self, elems):
        self.arr = elems

    def push_heap(self, i, j):
        d = abs(self.arr[i] - arr[j])
        heapq.heappush(self.heap, (-d, i, j))

    def pop_heap(self):
        return heapq.heappop(self.heap)

    def get_heap(self):
        return self.heap


n = int(input())
arr = [*map(int, input().split())]

in_arr  = [True] * n
l_neigh = [x for x in range(-1, n - 1)]
r_neigh = [x for x in range(1, n + 1)]

heap = Heap(n)
heap.pull(arr)
for i in range(n-1):
    heap.push_heap(i, i+1)

ans = 0
while heap.get_heap():
    d, i, j = heap.pop_heap()
    if not in_arr[i] or not in_arr[j]:
        continue

    ans       += -d
    in_arr[i] = False
    in_arr[j] = False

    l = l_neigh[i]
    r = r_neigh[j]

    if (0 <= l <= r <= n) and (in_arr[l] and in_arr[r]):
        heap.push_heap(l, r)
        r_neigh[l] = r
        l_neigh[r] = l

print(ans)
