from enum import Enum
from random import shuffle
from pprint import pprint


class Card:
    def __init__(self, rank, suit):
        super().__init__()
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return str(self.rank) + " " + str(self.suit)

    def __str__(self):
        return str(self.rank) + str(self.suit)


class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 15

    def symbol(self):
        if self is Rank.JACK:
            return 'J'
        elif self is Rank.QUEEN:
            return 'Q'
        elif self is Rank.KING:
            return 'K'
        elif self is Rank.ACE:
            return 'A'
        else:
            return str(self.value)


class Suit(Enum):
    CLUBS = 1
    SPADES = 2
    DIAMONDS = 3
    HEARTS = 4

    def symbol(self):
        if self is Suit.CLUBS:
            return '♣'
        elif self is Suit.SPADES:
            return '♠'
        elif self is Suit.DIAMONDS:
            return '♦'
        elif self is Suit.HEARTS:
            return '♥'

    def is_red(self):
        return self is Suit.DIAMONDS or self is Suit.HEARTS

    def is_black(self):
        return self is Suit.SPADES or self is Suit.CLUBS

    def is_different_color(self, suit):
        return suit.is_red() if self.is_black() else suit.is_black()


test_card = Card(Rank.THREE, Suit.CLUBS)


def main():
    deck = make_deck()
    stacks = make_stacks()


def make_stacks(deck):
    return [[deck.pop() for _ in range(i)] for i in range(1, 8)]


def make_deck():
    deck = []
    for c in Suit:
        for r in Rank:
            deck.append(Card(r, c))
    shuffle(deck)
    return deck


pprint(make_stacks(make_deck()))

















