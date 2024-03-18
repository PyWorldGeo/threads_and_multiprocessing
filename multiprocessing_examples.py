# importing the multiprocessing module
import multiprocessing
from multiprocessing import Process
#1


def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))


def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # creating processes
    p1 = Process(target=print_square, args=(10,))
    p2 = Process(target=print_cube, args=(10,))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print("Done!")

#2
# multiprocessing pool
def worker(num):
    return num**2

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    p = multiprocessing.Pool(2)
    values = p.map(func=worker, iterable=nums)
    p.close()
    print(values)

