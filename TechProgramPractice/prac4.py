from multiprocessing import Process, Queue
from array import array

file = open('3.txt', 'r+')
data = map(int, file.readlines())
m = array('i', [*data])
file.truncate(0)


def process_creator(input, output):
    fun, arr = input.get()
    print(fun, arr)
    output.put(fun(arr))
    print('Process finished', fun(arr))


class Numbers:
    @staticmethod
    def get_ranges(arr, num):
        ran = len(arr)//num
        return [arr[(i-1)*ran:i*ran] for i in range(1, num+1)]

    @staticmethod
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            left = [x for x in arr[1:] if x < pivot]
            right = [x for x in arr[1:] if x >= pivot]
            return Numbers.quicksort(left) + [pivot] + Numbers.quicksort(right)


def main(fun, ar):
    NUMBER_OF_PROCCES = 5
    TASKS = [(fun, arr) for arr in Numbers.get_ranges(ar, NUMBER_OF_PROCCES)]

    proc_run = Queue()
    proc_done = Queue()

    for task in TASKS:
        proc_run.put(task)

    for _ in range(NUMBER_OF_PROCCES):
        Process(target=process_creator, args=(proc_run, proc_done)).start()

    return proc_done


if __name__ == '__main__':
    proc_done = main(Numbers.quicksort, m)
    result = []
    for _ in range(5):
        result += proc_done.get()
    for elem in result:
        file.write(f'{elem}\n')