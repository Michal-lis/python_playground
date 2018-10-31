from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_perimeter(self):
        return round(2 * pi * self.radius, 2)

    def computer_area(self):
        return round(pi * pow(self.radius, 2))


a = Circle(5)
print(a.compute_perimeter())
print(a.computer_area())
