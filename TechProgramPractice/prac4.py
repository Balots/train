from multiprocessing import Process, Queue
from array import array

file = open('3.txt', 'r+')
data = map(int, file.readlines())
m = array('i', [*data]) # get data to array
file.truncate(0) # clear document


def process_creator(input, output):# Our interface to create processes
    fun, arr = input.get()
    print(fun, arr)
    output.put(fun(arr))
    print('Process finished', fun(arr))


class Numbers:
    @staticmethod
    def get_ranges(arr, num): # Divide array on num sub-arrays
        ran = len(arr)//num
        return [arr[(i-1)*ran:i*ran] for i in range(1, num+1)]

    @staticmethod
    def quicksort(arr): # QuickSort algorithm. Just like python sort()
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            left = [x for x in arr[1:] if x < pivot]
            right = [x for x in arr[1:] if x >= pivot]
            return Numbers.quicksort(left) + [pivot] + Numbers.quicksort(right)


def main(fun, ar):
    NUMBER_OF_PROCCES = 5
    TASKS = [(fun, arr) for arr in Numbers.get_ranges(ar, NUMBER_OF_PROCCES)] # Create tasks for queue

    proc_run = Queue() # Create queues
    proc_done = Queue()

    for task in TASKS:
        proc_run.put(task) # put tasks on queue

    for _ in range(NUMBER_OF_PROCCES):
        Process(target=process_creator, args=(proc_run, proc_done)).start() #start tasks from queue

    return proc_done


if __name__ == '__main__':
    proc_done = main(Numbers.quicksort, m) # get results
    result = []
    for _ in range(5):
        result += proc_done.get() # put them to list
    for elem in result:
        file.write(f'{elem}\n') # write them to the document