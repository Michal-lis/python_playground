def f1(f):
    def f2():
        print("poczatek f2")
        f()
        print("koniec f2")

    return f2


@f1
def f3():
    print("Marek aurelius")


f3 = f1(f3)
f3()
