from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def sale_offer(self, stock, shares, coll_code):
        pass

    @abstractmethod
    def buy_offer(self, stock, shares, coll_code):
        pass

    @abstractmethod
    def add_colleague(self, colleague):
        pass


class ConcreteMediator(Mediator):

    def sale_offer(self, stock, shares, coll_code):
        print(f"{shares} sold to colleague {coll_code} ")

    def buy_offer(self, stock, shares, coll_code):
        pass

    def add_colleague(self, colleague):
        self.colleagues.append(colleague)
        self.colleague_codes += 1
        colleague.set_colleague_code(self.colleague_codes)

    def __init__(self) -> None:
        self.colleagues = []
        self.colleague_codes = 0


class Colleague(ABC):
    def __init__(self, new_mediator):
        self.colleague_code = None
        self.mediator = new_mediator

    def sale_offer(self, stock, shares):
        self.mediator.sale_offer(stock, shares, self.colleague_code)

    def buy_offer(self, stock, shares):
        self.mediator.sale_offer(stock, shares, self.colleague_code)

    def set_colleague_code(self, coll_code):
        self.colleague_code = coll_code


class ConcreteColleague1(Colleague):
    def __init__(self, new_mediator):
        print("Colleague 1 signed up for stock exchange!")
        super().__init__(new_mediator)


class ConcreteColleague2(Colleague):
    def __init__(self, new_mediator):
        print("Colleague 2 signed up for stock exchange!")
        super().__init__(new_mediator)
