from abc import ABC, abstractmethod


class ATMState(ABC):
    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def eject_card(self):
        pass

    @abstractmethod
    def insert_pin(self, pin):
        pass

    @abstractmethod
    def request_cash(self, money):
        pass


class ATMMachine:
    def __init__(self) -> None:
        self.has_card = HasCard(self)
        self.no_card = NoCard(self)
        self.has_correct_pin = HasCorrectPin(self)
        self.atm_out_of_money = NoCash(self)
        self.cash_in_machine = 2000
        self.correct_pin_entered = False

        # initial state
        self.atm_state = self.no_card

        if self.cash_in_machine < 0:
            self.atm_state = self.atm_out_of_money

    def set_atm_state(self, new_atm_state):
        self.atm_state = new_atm_state

    def set_cash_in_machine(self, new_cash_in_machine):
        self.cash_in_machine = new_cash_in_machine

    def insert_card(self):
        self.atm_state.insert_card()

    def eject_card(self):
        self.atm_state.eject_card()

    def request_cash(self, cash_to_withdraw):
        self.atm_state.request_cash(cash_to_withdraw)

    def insert_pin(self, pin_entered):
        self.atm_state.insert_pin(pin_entered)

    def get_yes_card_state(self):
        print("State changed to")
        return self.has_card

    def get_no_card_state(self):
        return self.no_card

    def get_has_pin(self):
        return self.has_correct_pin

    def get_no_cash_state(self):
        return self.atm_out_of_money

    def present_state(self):
        print(self.atm_state)


class HasCard(ATMState):

    def __init__(self, new_atm_machine) -> None:
        self.atm_machine = new_atm_machine

    def insert_card(self):
        print("This ATM already has a card!")

    def eject_card(self):
        print("This ATM already has a card!")
        self.atm_machine.set_atm_state(self.atm_machine.get_no_card_state())

    def insert_pin(self, pin):
        print("The PIN you inserted is correct!")
        self.atm_machine.set_atm_state(self.atm_machine.get_has_pin())

    def request_cash(self, money):
        print("You must first enter a PIN!")

    def __repr__(self):
        return "has card state!"


class NoCard(ATMState):

    def insert_card(self):
        print("Inserting a card!")
        self.atm_machine.set_atm_state(self.atm_machine.get_yes_card_state())

    def eject_card(self):
        print("You must first enter a card before ejecting!")

    def insert_pin(self, pin):
        print("You must first insert a card before entering a PIN!")

    def request_cash(self, money):
        print("You must first insert a card before requesting cash!")

    def __init__(self, new_atm_machine) -> None:
        self.atm_machine = new_atm_machine

    def __repr__(self):
        return "no card state!"


class HasCorrectPin(ATMState):

    def insert_card(self):
        print("Card is already inserted!")

    def eject_card(self):
        print("You entered correct PIN, are you sure you want to eject card?")

    def insert_pin(self, pin):
        print("Correct pin has already been inserted")

    def request_cash(self, money):
        print("How much money would you like to withdraw?")

    def __init__(self, new_atm_machine) -> None:
        self.atm_machine = new_atm_machine

    def __repr__(self):
        return "has correct pin state!"


class NoCash(ATMState):

    def insert_card(self):
        print("Card is already inserted!")

    def eject_card(self):
        print("You entered correct PIN, are you sure you want to eject card?")

    def insert_pin(self, pin):
        print("Correct pin has already been inserted")

    def request_cash(self, money):
        print("How much money would you like to withdraw?")

    def __init__(self, new_atm_machine) -> None:
        self.atm_machine = new_atm_machine

    def __repr__(self):
        return "No cash state!"


class ATMProxy

a = ATMMachine()
a.present_state()
a.insert_card()
a.present_state()
