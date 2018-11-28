from abc import abstractmethod, ABC


class Subject(ABC):

    @abstractmethod
    def register(self, observer):
        pass

    @abstractmethod
    def unregister(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class StockGrabber(Subject):
    def __init__(self):
        self.observers = []
        self.ibmPrice = None
        self.aaplPrice = None
        self.googPrice = None

    def get_observer_idx_from_list(self, name):
        for idx, o in enumerate(self.observers):
            if o.name == name:
                return idx

    def register(self, new_observer):
        self.observers.append(new_observer)

    def unregister(self, delete_observer):
        idx = self.get_observer_idx_from_list(delete_observer)
        if not isinstance(idx, int):
            print("This observer is not on the observer list")
            return
        else:
            self.observers.remove(self.observers[idx])
            print(f"Observer {delete_observer} with index {idx + 1} removed")

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.ibmPrice, self.aaplPrice, self.googPrice)

    def set_ibm_price(self, price):
        self.ibmPrice = price
        self.notify_observers()

    def set_aaple_price(self, price):
        self.aaplPrice = price
        self.notify_observers()

    def set_goog_price(self, price):
        self.googPrice = price
        self.notify_observers()


class Observer(ABC):
    @abstractmethod
    def update(self, ibmPrice, aaplPrice, googPrice):
        pass


class StockObserver(Observer):
    def __init__(self, name, stock_grabber):
        self.name = name
        self.ibmPrice = None
        self.aaplPrice = None
        self.googPrice = None
        self.stock_grabber = stock_grabber
        self.stock_grabber.register(self)

    def __eq__(self, other):
        return self.name == other

    def update(self, ibmPrice, aaplPrice, googPrice):
        self.ibmPrice = ibmPrice
        self.aaplPrice = aaplPrice
        self.googPrice = googPrice
        self.print_the_prices()

    def print_the_prices(self):
        print(f"{self.name} prices:\n IBM: {self.ibmPrice}\n Apple: {self.aaplPrice}\n Google: {self.googPrice}")


if __name__ == '__main__':
    s = StockGrabber()
    mike = StockObserver('mike', s)
    darren = StockObserver('darren', s)
    s.set_aaple_price(31)
    s.set_goog_price(21)
    s.set_aaple_price(25)
    s.set_ibm_price(78)
    s.set_ibm_price(80)
    s.unregister(mike)
    s.set_ibm_price(76)
