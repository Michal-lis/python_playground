import random
import math


class Warrior(object):
    def __init__(self, name="Warrior", health=100, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)

        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt


class Battle(object):  # class method, no need to refer to self

    def startFight(self, warrior1, warrior2):

        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game over.")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game over.")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        damageToWarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)

        warriorB.health = warriorB.health - damageToWarriorB

        print("{} attack {} and deals {} damage".format(warriorA.name, warriorB.name, damageToWarriorB))

        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has died and {} is victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Keep fighting!"


def main():

    maximus = Warrior("Maximus", 50, 20, 10)

    cezar = Warrior("Cezar", 50, 20, 10)

    battle=Battle()

    battle.startFight(maximus,cezar)

main()
