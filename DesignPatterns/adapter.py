from abc import ABC, abstractmethod


class Fighter(ABC):
    @abstractmethod
    def attack(self, hitpoints):
        pass

    @abstractmethod
    def runaway(self):
        pass


class Warrior(Fighter):

    def __init__(self) -> None:
        self.name = "Warriorrr"

    def attack(self, hitpoints=5):
        print(f"Attacking for {hitpoints}")

    def runaway(self):
        print("Running away!")


class Orc:

    def __init__(self) -> None:
        self.name = "Typical Orc"

    def punch_with_face(self):
        print("Punching with orc's face!")


class OrcAdapter(Fighter):

    def __init__(self, orc) -> None:
        self.orc = orc

    def attack(self, hitpoints=3):
        self.orc.punch_with_face()

    def runaway(self):
        print("Orcs never run away!")


w = Warrior()
w.attack(5)
w.runaway()
o = Orc()
o.punch_with_face()
oa = OrcAdapter(o)
oa.attack()
