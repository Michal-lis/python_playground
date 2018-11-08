from multiprocessing import Pool


def f(n):
    return n * n


def calculate_5(li):
    pow5 = []
    for e in range(1000):
        a = e * 2 + pow(e, e)
        pow5.append(pow(li, 5))
    return pow5


if __name__ == '__main__':
    p = Pool()
    result = p.map(calculate_5, range(500))
    p.close()
    p.join()
    print(result)
