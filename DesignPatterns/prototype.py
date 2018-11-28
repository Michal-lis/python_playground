from copy import copy


class A:
    def __init__(self) -> None:
        self.name = "Mike"


a = A()
print(id(a))
b = copy(a)
print(id(b))
