from contextlib import contextmanager


class Open_files():
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


@contextmanager
def open_files(file, mode):
    f = open(file, mode)
    yield f
    f.close()


def gene():
    p = "aspdpaspd"
    yield p


# with open_files('data.txt', 'a') as f:
# f.write("matka boska czestochowska")

a = next(gene())
print(a)
a = next(gene())
print(a)
