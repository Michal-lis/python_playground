import threading
import time

ki = range(300)


def calculate_5(li):
    pow5 = []
    for e in li:
        for e in li:
            for e in li:
                pow5.append(pow(e, 5))
    return pow5


def calculate_4(li):
    pow4 = []
    for e in li:
        for e in li:
            for e in li:
                pow4.append(pow(e, 4))
    return pow4


thread1 = threading.Thread(target=calculate_5, args=(ki,))
thread2 = threading.Thread(target=calculate_4, args=(ki,))

tt_init_5 = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
tt_end_5 = time.time()
tt5 = tt_end_5 - tt_init_5

t_init_5 = time.time()
a5 = calculate_5(ki)
t_end_5 = time.time()
t5 = t_end_5 - t_init_5

t_init_4 = time.time()
a4 = calculate_4(ki)
t_end_4 = time.time()
t4 = t_end_4 - t_init_4

print(t4)
print(t5)
print(tt5)
