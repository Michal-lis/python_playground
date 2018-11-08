import multiprocessing
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


p1 = multiprocessing.Process(target=calculate_5, args=(ki,))
p2 = multiprocessing.Process(target=calculate_4, args=(ki,))
p3 = multiprocessing.Process(target=calculate_4, args=(ki,))
p4 = multiprocessing.Process(target=calculate_4, args=(ki,))
# p5 = multiprocessing.Process(target=calculate_4, args=(ki,))

tt_init_5 = time.time()
p1.start()
p2.start()
p3.start()
p4.start()
# p4.start()
p1.join()
p2.join()
p3.join()
p4.join()
# p4.join()
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
