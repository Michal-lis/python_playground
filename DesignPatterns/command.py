from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class TurnTVOn(Command):

    def __init__(self, electronic_device) -> None:
        self.electronic_device = electronic_device

    def execute(self):
        self.electronic_device.on()


class DeviceButton:

    def __init__(self, command) -> None:
        self.command = command

    def press(self):
        self.command.execute()


class ElectronicDevice(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass


class Television(ElectronicDevice):
    # Receiver
    def on(self):
        print("Turning on")

    def off(self):
        print("Turning off")

    def volume_up(self):
        self.volume += 1
        print("Voluming up!")

    def volume_down(self):
        self.volume -= 1
        print("Voluming down!")

    def __init__(self, volume) -> None:
        self.volume = volume

    def __repr__(self) -> str:
        return str(self.volume)
