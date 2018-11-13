from Piece import Pawn, Bishop, Knight, Rook, King, Queen
from utils import WHITE, BLACK, letters, numbers, convert_l_n_to_indexes


class Board:

    def __init__(self) -> None:
        self.board = self.generate_board()

    def __repr__(self):
        repr = ""
        for number in reversed(numbers):
            line = str(number) + "  " + chr(9122)
            for letter in letters:
                line += "  " + str(self.get_square(letter, number))
            line += "\n"
            repr += line
        repr += "    " + chr(9148) * 33 + "\n       " + chr(9398) + "  " + chr(9399) + "  " + chr(
            9400) + "  " + chr(9401) + "  " + chr(
            9402) + "  " + chr(9403) + "  " + chr(9404) + "  " + chr(9405)
        return repr

    def generate_board(self):
        board = [[] for _ in range(8)]
        for idx, letter in enumerate(letters):
            for x in range(8):
                board[idx].append(Square(letter, x + 1))
        return board

    def initialize_starting_board(self):
        for letter in letters:
            self.set_piece_on_square(letter, 7, Pawn(BLACK))
            self.set_piece_on_square(letter, 2, Pawn(WHITE))
        for letter in ['a', 'h']:
            self.set_piece_on_square(letter, 1, Bishop(WHITE))
            self.set_piece_on_square(letter, 8, Bishop(BLACK))
        for letter in ['b', 'g']:
            self.set_piece_on_square(letter, 1, Knight(WHITE))
            self.set_piece_on_square(letter, 8, Knight(BLACK))
        for letter in ['c', 'f']:
            self.set_piece_on_square(letter, 1, Rook(WHITE))
            self.set_piece_on_square(letter, 8, Rook(BLACK))
        self.set_piece_on_square('d', 1, Queen(WHITE))
        self.set_piece_on_square('e', 8, Queen(BLACK))
        self.set_piece_on_square('e', 1, King(WHITE))
        self.set_piece_on_square('d', 8, King(BLACK))

    def check_if_occupied(self, l, n):
        x_axis, y_axis = convert_l_n_to_indexes(l, n)
        return self.board[x_axis][y_axis].is_occupied()

    def check_is_king_alive(self, destination, king_killed=False, color_loosing=None):
        piece_killed = self.get_square(destination[0], destination[1]).get_piece()
        if piece_killed and isinstance(piece_killed, King):
            color_loosing = piece_killed.get_color()
            king_killed = True
        return king_killed, color_loosing

    def check_if_castling(self, field_chosen, destination):
        if (field_chosen == ('e', 1) and destination in [('a', 1), ('h', 1)]) or (
                field_chosen == ('d', 8) and destination in [('a', 8), ('h', 8)]):
            return True
        return False

    def execute_move(self, field_chosen, destination, piece_chosen):
        castling = self.check_if_castling(field_chosen, destination)
        if (isinstance(piece_chosen, Pawn) and destination[1] == field_chosen[1] + 2):
            pass

        if not castling:
            self.set_piece_on_square(destination[0], destination[1], piece_chosen)
            self.get_square(field_chosen[0], field_chosen[1]).set_square_free()
        else:
            temp_piece = self.get_piece_from_square(destination[0], destination[1])
            self.set_piece_on_square(destination[0], destination[1], piece_chosen)
            self.set_piece_on_square(field_chosen[0], field_chosen[1], temp_piece)

    def get_square(self, l, n):
        x_axis, y_axis = convert_l_n_to_indexes(l, n)
        return self.board[x_axis][y_axis]

    def get_piece_from_square(self, l: str, n: int):
        x_axis, y_axis = convert_l_n_to_indexes(l, n)
        return self.board[x_axis][y_axis].get_piece()

    def set_piece_on_square(self, l: str, n: int, piece):
        x_axis, y_axis = convert_l_n_to_indexes(l, n)
        o = self.board[x_axis][y_axis]
        o.set_piece(piece)

    def validate_piece_choice(self, field_chosen, current_player):
        letter_from = field_chosen[0]
        number_from = field_chosen[1]
        piece_chosen = self.get_piece_from_square(letter_from, number_from)
        if not piece_chosen:
            print("There is no piece on this field!")
            return False
        if piece_chosen.get_color() != current_player.get_color():
            print("The chosen piece belongs to your opponent!")
            return False
        return True


class Square:

    def __init__(self, letter, number, occupied=False, piece=None):
        self.letter = letter
        self.number = str(number)
        self.occupied = occupied
        self.piece = piece

    def __repr__(self):
        if self.occupied:
            return self.piece.get_sign()
        else:
            return "  "

    def get_letter(self):
        return self.letter

    def get_number(self):
        return self.number

    def is_occupied(self):
        return self.occupied

    def get_piece(self):
        if self.occupied == False:
            return None
        elif self.occupied == True:
            return self.piece

    def set_piece(self, piece):
        self.piece = piece
        self.occupied = True

    def set_square_free(self):
        self.piece = None
        self.occupied = False
