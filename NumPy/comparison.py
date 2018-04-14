import numpy as np
import time
import sys


def memory_storage():
    l = list(range(1000))
    print(sys.getsizeof(l[50]) * len(l))
    # 28000 bytes, one pointer is 28 bytes

    l = list(range(1000))
    l.append('DUASDASDASDASDADSA')
    k = l
    print(sys.getsizeof(k[50]) * len(k))

    a = np.array(l)
    print(a.size * a.itemsize)
    # 4000 bytes, one is 4 bytes only


def time_comparison(size, type=None):
    if type == 'init':
        ldeclaration_start = time.time()
        l1 = range(size)
        ldeclaration_end = time.time()

        adeclaration_start = time.time()
        a1 = np.array(l1)
        adeclaration_end = time.time()
        print("Declaration list: {}".format((ldeclaration_end - ldeclaration_start) * 1000))
        print("Declaration array: {}".format((adeclaration_end - adeclaration_start) * 1000))
    if type == 'add':
        l1 = range(size)
        l2 = range(size)
        ldeclaration_start = time.time()
        result = [(x + y) for x, y in zip(l1, l2)]
        ldeclaration_end = time.time()

        a1 = np.array(l1)
        a2 = np.array(l2)
        adeclaration_start = time.time()
        result = a1 + a2
        adeclaration_end = time.time()
        print("Declaration list: {}".format((ldeclaration_end - ldeclaration_start) * 1000))
        print("Declaration array: {}".format((adeclaration_end - adeclaration_start) * 1000))


if __name__ == '__main__':
    time_comparison(1000000, type='add')
    # conclusion: on 1 000 000 integers np array is 10 times faster
