from multiprocessing import Process, Queue
from array import array

m = array('i', [12, 34, 5, 6, 78, 3, 23, 46, 79, 56])


def get_elem(arr):
    return len(arr)


def process_creator(input, output):
    fun, arr = input.get()
    print(fun, arr)
    output.put(fun(arr))
    print('Process finished', fun(arr))

def main():
    proc_run = Queue()
    proc_done = Queue()

    results = m
    TASKS = [(get_elem, arr) for arr in [results[:len(results) // 2], results[len(results) // 2:]]]
    for task in TASKS:
        proc_run.put(task)

    for _ in range(len(TASKS)):
        Process(target=process_creator, args=(proc_run, proc_done)).start()

    s = 0
    for _ in range(len(TASKS)):
        s += proc_done.get()
    return s


if __name__ == '__main__':
    print(main())