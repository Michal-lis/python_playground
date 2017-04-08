from enum import Enum


class Card:
    def __init__(self, rank, color):
        super().__init__()
        self.color = color
        self.rank = rank


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


class Color(Enum):
    CLUBS = 1
    SPADES = 2
    DIAMONDS = 3
    HEARTS = 4

    def is_red(self):
        return self == Color.DIAMONDS or self == Color.HEARTS

    def is_black(self):
        return self == Color.SPADES or self == Color.CLUBS

    def is_different_color(self, color):
        return color.is_red() if self.is_black() else color.is_black()
