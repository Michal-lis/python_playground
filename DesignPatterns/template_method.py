from abc import ABC, abstractmethod


class Sandwich(ABC):
    def make_sandwich(self):
        self.cut_bun()
        if self.customer_wants_meat():
            self.add_meat()
        if self.customer_wants_veggies():
            self.add_veggies()
        self.wrap_the_sandwich()

    def cut_bun(self):
        print("Bun is cut")

    @abstractmethod
    def customer_wants_meat(self):
        pass

    @abstractmethod
    def add_meat(self):
        pass

    @abstractmethod
    def add_veggies(self):
        pass

    @abstractmethod
    def customer_wants_veggies(self):
        pass


class ItalianSandwich(Sandwich):

    def customer_wants_meat(self):
        pass

    def add_meat(self):
        pass

    def add_veggies(self):
        pass

    def customer_wants_veggies(self):
        pass
