from multiprocessing import Process, Queue
from array import array

m = array('i', [12, 34, 5, 6, 78, 3, 23, 46, 79, 56])


def get_elem(arr): # Get length of array
    return len(arr)


def process_creator(input, output): # Our interface to create processes
    fun, arr = input.get()
    print(fun, arr)
    output.put(fun(arr))
    print('Process finished', fun(arr))

def main():
    proc_run = Queue() # Get queues to control results of processes
    proc_done = Queue()

    results = m
    TASKS = [(get_elem, arr) for arr in [results[:len(results) // 2], results[len(results) // 2:]]] # Divide array on two vision blocks
    for task in TASKS: # Add functions and their arguments to put on processes
        proc_run.put(task)

    for _ in range(len(TASKS)):
        Process(target=process_creator, args=(proc_run, proc_done)).start() # Start processes

    s = 0 # Here's we're summing results
    for _ in range(len(TASKS)):
        s += proc_done.get() # get result from queue
    return s


if __name__ == '__main__':
    print(main())