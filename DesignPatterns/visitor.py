from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit(self, item):
        pass


class TaxVisitor(Visitor):
    def visit(self, item):
        if isinstance(item, Necessity):
            tax = item.value * 0.25
        if isinstance(item, Tobacco):
            tax = item.value * 0.05
        if isinstance(item, Liquor):
            tax = item.value * 0.2
        print("Value added tax for " + item.name + " is equal to " + str(tax))

    def __init__(self) -> None:
        pass


class Visitable(ABC):
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

    def accept(self, visitor):
        visitor.visit(self)


class Necessity(Visitable): pass


class Tobacco(Visitable): pass


class Liquor(Visitable): pass


tax_visitor = TaxVisitor()
marlboro = Tobacco("Marlboro", 5)
marlboro.accept(tax_visitor)
baileys = Liquor("Bailey's", 5)
baileys.accept(tax_visitor)
nappy = Necessity("Nappy", 2)
nappy.accept(tax_visitor)
