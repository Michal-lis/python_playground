import itertools
from .utils import WHITE


class Piece:
    newid = itertools.count()

    def __init__(self, name, sign, color):
        self.id = next(Piece.newid)
        self.name = name
        self.sign = sign
        self.color = color

    def get_color(self):
        return self.color

    def get_sign(self):
        return self.sign

    @staticmethod
    def calculate_sign(num, color):
        char_num = num + 6 if color == BLACK else num
        return " " + chr(char_num)

    def get_possible_moves(self):
        pass


class Pawn(Piece):

    def __init__(self, color):
        name = "Pawn"
        sign = self.calculate_sign(9817, color)
        super().__init__(name, sign, color)

    def get_possible_moves(self):
        pass


class Bishop(Piece):

    def __init__(self, color):
        name = "Bishop"
        sign = self.calculate_sign(9814, color)
        super().__init__(name, sign, color)

    def get_possible_moves(self):
        pass


class Knight(Piece):

    def __init__(self, color):
        name = "Knight"
        sign = self.calculate_sign(9816, color)
        super().__init__(name, sign, color)

    def get_possible_moves(self):
        pass


class Rook(Piece):

    def __init__(self, color):
        name = "Rook"
        sign = self.calculate_sign(9815, color)
        super().__init__(name, sign, color)

    def get_possible_moves(self):
        pass


class Queen(Piece):

    def __init__(self, color):
        name = "Queen"
        sign = self.calculate_sign(9813, color)
        super().__init__(name, sign, color)

    def get_possible_moves(self):
        pass


class King(Piece):

    def __init__(self, color):
        name = "King"
        sign = self.calculate_sign(9812, color)
        super().__init__(name, sign, color)

    def get_possible_moves(self):
        pass
