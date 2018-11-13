import inspect


class Pizza(object):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


class Calzone(Pizza):
    def get_size(self,c):
        a = super().get_size()
        return a, a



pizza = Pizza(32)
cal = Calzone(32)
pizza.get_size()
cal.get_size(5)


def mike(name, old="mike"):
    print(name)
    print(old)
    return old


print(inspect.signature(mike))
