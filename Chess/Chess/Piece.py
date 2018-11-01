import itertools
from utils import WHITE, convert_l_n_to_indexes, convert_indexes_to_l_n, is_within_board


class Piece:
    newid = itertools.count()

    def __init__(self, name, sign, color):
        self.id = next(Piece.newid)
        self.name = name
        self.sign = sign
        self.color = color

    def __repr__(self):
        return str(self.id) + " " + self.sign

    def get_color(self):
        return self.color

    def get_sign(self):
        return self.sign

    @staticmethod
    def calculate_sign(num, color):
        char_num = num + 6 if color == WHITE else num
        return " " + chr(char_num)

    def get_possible_moves(self, field, board):
        pass


class Pawn(Piece):

    def __init__(self, color):
        name = "Pawn"
        sign = self.calculate_sign(9817, color)
        super().__init__(name, sign, color)

    def get_possible_moves(self, field, board):
        possible_moves = []
        letter = field[0]
        number = field[1]
        x_initial, y_initial = convert_l_n_to_indexes(letter, number)

        # step forward
        x = x_initial
        y = y_initial + 1
        if is_within_board(x, y):
            l, n = convert_indexes_to_l_n(x, y)
            occupied = board.check_if_occupied(l, n)
            if not occupied:
                possible_moves.append((l, n))

        # attack to right
        x = x_initial + 1
        y = y_initial + 1
        if is_within_board(x, y):
            l, n = convert_indexes_to_l_n(x, y)
            piece = board.get_square_content(l, n)
            if piece and piece.get_color() != self.color:
                possible_moves.append((l, n))

        # attack to left
        x = x_initial - 1
        y = y_initial + 1

        if is_within_board(x, y):
            l, n = convert_indexes_to_l_n(x, y)
            piece = board.get_square_content(l, n)
            if piece and piece.get_color() != self.color:
                possible_moves.append((l, n))

        print(possible_moves)


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
