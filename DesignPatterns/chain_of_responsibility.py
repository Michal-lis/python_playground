from abc import ABC, abstractmethod


class Chain(ABC):
    @abstractmethod
    def set_next_chain(self, next_chain):
        pass

    @abstractmethod
    def calculate(self, request):
        pass


class Numbers:
    def __init__(self, number1, number2, calculation_wanted):
        self.number1 = number1
        self.number2 = number2
        self.calculation_wanted = calculation_wanted

    def get_number1(self):
        return self.number1

    def get_number2(self):
        return self.number2

    def get_calc_wanted(self):
        return self.calculation_wanted


class AddNumbers(Chain):
    def set_next_chain(self, next_chain):
        self.next_chain = next_chain

    def calculate(self, request):
        if request.get_calc_wanted() == "add":
            print(
                f"{request.get_number1()}" + " + " + f"{request.get_number2()}" + " = " + f"{request.get_number2() + request.get_number1()}")
        else:
            print("passing to the next")
            chain2 = DivNumbers()
            self.set_next_chain(chain2)
            self.next_chain.calculate(request)

    def __init__(self) -> None:
        self.next_chain = None


class DivNumbers(Chain):
    def set_next_chain(self, next_chain):
        self.next_chain = next_chain

    def calculate(self, request):
        if request.get_calc_wanted() == "div":
            print(
                f"{request.get_number1()}" + " / " + f"{request.get_number2()}" + " = " + f"{request.get_number2() / request.get_number1()}")
        else:
            print("passing to the next")
            chain3 = SubNumbers()
            self.set_next_chain(chain3)
            self.next_chain.calculate(request)

    def __init__(self) -> None:
        self.next_chain = None


class SubNumbers(Chain):
    def set_next_chain(self, next_chain):
        self.next_chain = next_chain

    def calculate(self, request):
        if request.get_calc_wanted() == "sub":
            print(
                f"{request.get_number1()}" + " - " + f"{request.get_number2()}" + " = " + f"{request.get_number2() - request.get_number1()}")
        else:
            print("passing to the next")
            chain3 = MultNumbers()
            self.set_next_chain(chain3)
            self.next_chain.calculate(request)

    def __init__(self) -> None:
        self.next_chain = None


class MultNumbers(Chain):
    def set_next_chain(self, next_chain):
        self.next_chain = next_chain

    def calculate(self, request):
        if request.get_calc_wanted() == "mult":
            print(
                f"{request.get_number1()}" + " * " + f"{request.get_number2()}" + " = " + f"{request.get_number2() * request.get_number1()}")
        else:
            print("End of the chain")
            exit()

    def __init__(self) -> None:
        self.next_chain = None


chain1 = AddNumbers()
req = Numbers(2, 3, 'sub')
chain1.calculate(req)
