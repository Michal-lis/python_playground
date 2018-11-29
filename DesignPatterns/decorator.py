from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class PlainPizza(Pizza):
    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

    def __init__(self, cost, description) -> None:
        self.cost = cost
        self.description = description

    def __repr__(self):
        return str(self.cost) + " " + self.description


class ToppingDecorator(Pizza, ABC):
    def __init__(self, pizza):
        self.temp_pizza = pizza

    def get_cost(self):
        return self.temp_pizza.get_cost()

    def get_description(self):
        return self.temp_pizza.get_cost()

    def __repr__(self):
        return str(self.temp_pizza)


class Mozarella(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.temp_pizza.description = self.temp_pizza.get_description() + " mozarella"
        self.temp_pizza.cost = self.temp_pizza.get_cost() + 0.5


pi = PlainPizza(31, 'old and stinky')
print(pi)
moz = Mozarella(pi)
print(moz)
