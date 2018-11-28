from abc import ABC, abstractmethod
import random


class EnemyShipFactory:
    def __init__(self):
        self.enemy_ship = None

    def make_enemy_ship(self, typ):
        if typ == 'U':
            self.enemy_ship = UFOEnemyShip()
        elif typ == 'R':
            self.enemy_ship = RocketEnemyShip()
        return self.enemy_ship


class EnemyShip(ABC):
    def __init__(self, name, amt_damage):
        self._name = name
        self._amt_damage = amt_damage

    def get_name(self):
        return self._name

    def get_damage(self):
        return self._amt_damage

    def follow_hero_ship(self):
        print(f"{self.get_name()} is following the hero")

    def display_enemy_ship(self):
        print(f"{self.get_name()} is on the screen")

    def enemy_ship_shoots(self):
        print(f"{self.get_name()} attacks and does {self.get_damage()}")


class UFOEnemyShip(EnemyShip):
    def __init__(self):
        super().__init__("UFO Enemy Ship", random.randrange(10, 21))


class RocketEnemyShip(EnemyShip):
    def __init__(self):
        super().__init__("Rocket Enemy Ship", random.randrange(1, 11))


if __name__ == '__main__':
    factory = EnemyShipFactory()
    typ = None
    while typ != "":
        typ = input("Which type should be built now?")
        enemy_ship = factory.make_enemy_ship(typ)
        enemy_ship.display_enemy_ship()
        enemy_ship.follow_hero_ship()
        enemy_ship.enemy_ship_shoots()
