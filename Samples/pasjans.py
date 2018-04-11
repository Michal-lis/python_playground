from enum import Enum
from random import shuffle
from pprint import pprint
from typing import List


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

    def __str__(self) -> str:
        if self is Rank.JACK:
            return 'J'
        elif self is Rank.QUEEN:
            return 'Q'
        elif self is Rank.KING:
            return 'K'
        elif self is Rank.ACE:
            return 'A'
        else:
            # for all other ranks, the display string is equal to the enum value
            return str(self.value)

    def is_followed_by(self, other_rank: 'Rank') -> bool:
        """True iff other_rank is one higher than self"""
        return self.value + 1 == other_rank.value


class Suit(Enum):
    CLUBS = 1
    SPADES = 2
    DIAMONDS = 3
    HEARTS = 4

    def __str__(self) -> str:
        if self is Suit.CLUBS:
            return '♣'
        elif self is Suit.SPADES:
            return '♠'
        elif self is Suit.DIAMONDS:
            return '♦'
        elif self is Suit.HEARTS:
            return '♥'

    def is_red(self) -> bool:
        return self is Suit.DIAMONDS or self is Suit.HEARTS

    def is_black(self) -> bool:
        return self is Suit.SPADES or self is Suit.CLUBS

    def is_different_color(self, suit: 'Suit') -> bool:
        return suit.is_red() if self.is_black() else suit.is_black()


class Card:
    def __init__(self, rank: Rank, suit: Suit) -> None:
        super().__init__()
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        """For debugging purposes"""
        return str(self.rank) + " " + str(self.suit)

    def __str__(self) -> str:
        """For displaying purposes"""
        return (str(self.rank) + str(self.suit)).rjust(4)


def show_stacks(stacks: List[List[Card]]) -> List[str]:
    """Returns standard repr of the seven stacks, each laid out vertically."""
    lines = []
    max_stack_len = max(len(s) for s in stacks)  # this is how many rows we need
    for i in range(max_stack_len):  # iteration of this loop corresponds to a row of text
        line = ''
        for j in range(7):  # to build the row, we take one card from each stack, if the stack has at least i cards
            if len(stacks[j]) > i:
                line += str(stacks[j][i])
            else:
                line += '    '  # placeholder for alignment
        lines.append(line)
    return lines


def make_stacks(deck: List[Card]) -> List[List[Card]]:
    """Note: this methods mutates `deck`"""
    return [[deck.pop() for _ in range(i)] for i in range(1, 8)]


def make_deck() -> List[Card]:
    deck = []
    for c in Suit:
        for r in Rank:
            deck.append(Card(r, c))
    shuffle(deck)
    return deck


def main():
    deck = make_deck()
    stacks = make_stacks(deck)
    lines = show_stacks(stacks)
    for line in lines:
        print(line)


test_card = Card(Rank.THREE, Suit.CLUBS)

if __name__ == '__main__':
    main()
