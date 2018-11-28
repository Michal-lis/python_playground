from abc import ABC, abstractmethod


class Animal:
    @abstractmethod
    def __init__(self, name):
        pass

    def set_flying_type(self, type):
        self._fly_type = type

    def try_to_fly(self):
        return self._fly_type.fly()


class ItFlys:
    def fly(self):
        print("I can fly")


class CantFly:
    def fly(self):
        print("Can't fly")


class Dog(Animal):
    def __init__(self, name):
        self._name = "Dogname " + str(name)
        self._fly_type = CantFly()

    def __str__(self):
        return self._name


class Bird(Animal):
    def __init__(self, name):
        self._name = "Birdname " + name
        self._fly_type = ItFlys()

    def __str__(self):
        return self._name


# you could inherit from 2 classes in which one of these would be flying class but this way you
# couldn't change the flying property of the class during its lifetime!
k = Bird('mike')
k.try_to_fly()
k.set_flying_type(CantFly())
k.try_to_fly()
print(k)
