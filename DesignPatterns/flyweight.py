class Shape:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name


class Color:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name


class Figure:
    def __init__(self, shape, color) -> None:
        self.shape = shape
        self.color = color

    def __repr__(self) -> str:
        return str(self.shape) + str(self.color)
