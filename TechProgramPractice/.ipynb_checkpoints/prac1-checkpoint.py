from multiprocessing import Process, Queue
from array import array

main_pull = array('i', [12, 34, 5, 6, 78, 3, 23, 46, 79, 56])


class Numbers:
    @staticmethod
    def get_max(arr):
        m = arr[0]
        for elem in arr[1:]:
            m = (m, elem)[elem > m]
        return m


def process_creator(input, output):
    fun, arr = input.get()
    print(fun, arr)
    output.put(fun(arr))
    print('Process finished', fun(arr))


def test():
    NUMBER_OF_PROCESS = 2

    proc_run = Queue()
    proc_done = Queue()

    results = main_pull
    while len(results) != 2:
        TASKS = [(Numbers.get_max, arr) for arr in [results[:len(results) // 2], results[len(results) // 2:]]]
        for task in TASKS:
            proc_run.put(task)

        for _ in range(NUMBER_OF_PROCESS):
            Process(target=process_creator, args=(proc_run, proc_done)).start()

        results = []
        for _ in range(NUMBER_OF_PROCESS):
            results.append(proc_done.get())
        print(results)
    else:
        print(Numbers.get_max(results))


if __name__ == '__main__':
    test()

