from multiprocessing import Process, Queue
from array import array

file = open('3.txt', 'r')
data = map(int, file.readlines())
m = array('i', [*data])
file.close() # Get data from text


def process_creator(input, output):
    fun, arr = input.get()
    print(fun, arr)
    output.put(fun(arr))
    print('Process finished', fun(arr)) # Our interface to create processes


class Numbers:
    @staticmethod
    def get_max(arr):
        m = arr[0]
        for elem in arr[1:]:
            m = (m, elem)[elem > m]
        return m # Puzirek for get max value from array

    @staticmethod
    def get_elem(arr):
        return len(arr) # Get length of array

    @staticmethod
    def get_ranges(arr, num): # Divide array on num sub-arrays
        ran = len(arr)//num
        return [arr[(i-1)*ran:i*ran] for i in range(1, num+1)]


def main(fun, ar):
    NUMBER_OF_PROCCES = 5
    TASKS = [(fun, arr) for arr in Numbers.get_ranges(ar, NUMBER_OF_PROCCES)] # Create tasks for queue

    proc_run = Queue() # Create queues
    proc_done = Queue()

    for task in TASKS:
        proc_run.put(task) # Add functions and their arguments to put on processes

    for _ in range(NUMBER_OF_PROCCES):
        Process(target=process_creator, args=(proc_run, proc_done)).start() # start processes

    return proc_done


if __name__ == '__main__':
    # MAX VALUE
    result = m
    while len(result) != 5:
        proc_done = main(Numbers.get_max, result) # get all results
        result = []
        for _ in range(5):
            result.append(proc_done.get()) # append them to list
    else:
        print(f'Max Value in massive is {Numbers.get_max(result)}') # get max value when there is 5 elements in array

    # NUMBER OF VALUES
    s = 0
    proc_done = main(Numbers.get_elem, m)
    for _ in range(5):
        s += proc_done.get() # summary of all elements
    print(f'Number of elems is {s}')


