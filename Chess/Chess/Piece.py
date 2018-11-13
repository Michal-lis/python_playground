import itertools
from utils import WHITE, BLACK, convert_l_n_to_indexes, convert_indexes_to_l_n, is_within_board


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

    def prepare_x_y_initial(self, current_field):
        letter = current_field[0]
        number = current_field[1]
        return convert_l_n_to_indexes(letter, number)

    def get_possible_moves(self, current_field, board, modifications, limit=None):
        x_initial, y_initial = self.prepare_x_y_initial(current_field)
        possible_moves = []
        for modification in modifications:
            x = x_initial
            y = y_initial
            stop = False
            while not stop:
                x, y = modification(x, y)
                if is_within_board(x, y):
                    l, n = convert_indexes_to_l_n(x, y)
                    piece = board.get_piece_from_square(l, n)
                    # free square without piece
                    if not piece:
                        possible_moves.append((l, n))
                    # enemy piece encountered
                    elif piece and piece.get_color() != self.color:
                        possible_moves.append((l, n))
                        break
                    # ally piece encountered
                    else:
                        break
                    # for king only:
                    if limit:
                        break
                else:
                    break
        return possible_moves

    def go_left(self, x, y):
        return x - 1, y

    def go_right(self, x, y):
        return x + 1, y

    def go_down(self, x, y):
        return x, y - 1

    def go_up(self, x, y):
        return x, y + 1

    def go_left_up(self, x, y):
        return x - 1, y + 1

    def go_right_up(self, x, y):
        return x + 1, y + 1

    def go_left_down(self, x, y):
        return x - 1, y - 1

    def go_right_down(self, x, y):
        return x + 1, y - 1


class Pawn(Piece):

    def __init__(self, color):
        name = "Pawn"
        sign = self.calculate_sign(9817, color)
        super(Pawn, self).__init__(name, sign, color)
        self.en_passant = False

    def set_en_passant_possible(self):
        self.en_passant = True

    def get_en_passant_possible(self):
        return self.en_passant

    def get_possible_moves(self, current_field, board):
        x_initial, y_initial = super(Pawn, self).prepare_x_y_initial(current_field)
        possible_moves = []
        if self.get_color() == BLACK:
            sign = -1
        else:
            sign = 1

        # double step forward when initial position
        if (self.get_color() == WHITE and y_initial == 1) or (self.get_color() == BLACK and y_initial == 6):
            x = x_initial
            y = y_initial + 2 * sign
            if is_within_board(x, y):
                l, n = convert_indexes_to_l_n(x, y)
                occupied = board.check_if_occupied(l, n)
                if not occupied:
                    possible_moves.append((l, n))

        # step forward
        x = x_initial
        y = y_initial + 1 * sign
        if is_within_board(x, y):
            l, n = convert_indexes_to_l_n(x, y)
            occupied = board.check_if_occupied(l, n)
            if not occupied:
                possible_moves.append((l, n))

        # attack to right
        x = x_initial + 1
        y = y_initial + 1 * sign
        if is_within_board(x, y):
            l, n = convert_indexes_to_l_n(x, y)
            piece = board.get_piece_from_square(l, n)
            if piece and piece.get_color() != self.color:
                possible_moves.append((l, n))

        # attack to left
        x = x_initial - 1
        y = y_initial + 1 * sign

        if is_within_board(x, y):
            l, n = convert_indexes_to_l_n(x, y)
            piece = board.get_piece_from_square(l, n)
            if piece and piece.get_color() != self.color:
                possible_moves.append((l, n))

        # en_passant
        pass

        return possible_moves


class Knight(Piece):

    def __init__(self, color):
        name = "Knight"
        sign = self.calculate_sign(9816, color)
        super(Knight, self).__init__(name, sign, color)

    def get_possible_moves(self, current_field, board):
        possible_moves = []
        x_initial, y_initial = super(Knight, self).prepare_x_y_initial(current_field)
        """
         # #
        #   #
          O
        #   #
         # #   
        """
        x = x_initial
        y = y_initial
        possibilities = ((x - 1, y + 2), (x + 1, y + 2),
                         (x - 2, y + 1), (x + 2, y + 1),
                         (x - 2, y - 1), (x + 2, y - 1),
                         (x - 1, y - 2), (x + 1, y - 2))
        for (x, y) in possibilities:
            if is_within_board(x, y):
                l, n = convert_indexes_to_l_n(x, y)
                piece = board.get_piece_from_square(l, n)
                if (not piece) or (piece and piece.get_color() != self.color):
                    possible_moves.append((l, n))
        return possible_moves


class Bishop(Piece):

    def __init__(self, color):
        name = "Bishop"
        sign = self.calculate_sign(9814, color)
        super(Bishop, self).__init__(name, sign, color)

    def get_possible_moves(self, current_field, board):
        """
                  #
                  #
                  #
            # # # O # # #
                  #
                  #
                  #
        """
        movement = (self.go_left, self.go_right, self.go_down, self.go_up)
        return super(Bishop, self).get_possible_moves(current_field, board, movement)


class Rook(Piece):

    def __init__(self, color):
        name = "Rook"
        sign = self.calculate_sign(9815, color)
        super(Rook, self).__init__(name, sign, color)

    def get_possible_moves(self, current_field, board):
        """
               #     #
                #   #
                  O
                #   #
               #     #
        """
        movement = [self.go_left_up, self.go_right_up, self.go_left_down, self.go_right_down]
        return super(Rook, self).get_possible_moves(current_field, board, movement)


class Queen(Piece):

    def __init__(self, color):
        name = "Queen"
        sign = self.calculate_sign(9813, color)
        super(Queen, self).__init__(name, sign, color)

    def get_possible_moves(self, current_field, board):
        """
           #  #  #
            # # #
        # # # O # # #
            # # #
           #  #  #
        """
        movement = (self.go_left_up, self.go_right_up, self.go_left_down, self.go_right_down,
                    self.go_left, self.go_right, self.go_down, self.go_up)
        return super(Queen, self).get_possible_moves(current_field, board, movement)


class King(Piece):

    def __init__(self, color):
        name = "King"
        sign = self.calculate_sign(9812, color)
        super(King, self).__init__(name, sign, color)
        self.en_passant_possible = True

    def get_possible_moves(self, current_field, board):
        """
            # # #
            # O #
            # # #
        """
        movement = (self.go_left_up, self.go_right_up, self.go_left_down, self.go_right_down,
                    self.go_left, self.go_right, self.go_down, self.go_up)
        limit = 1
        possible_moves = super(King, self).get_possible_moves(current_field, board, movement, limit)
        if self.get_color() == WHITE:
            self.check_castling_possible(board, 'a', 1, WHITE, ['b', 'c', 'd'], possible_moves)
            self.check_castling_possible(board, 'h', 1, WHITE, ['g', 'f'], possible_moves)
        elif self.get_color() == BLACK:
            self.check_castling_possible(board, 'a', 8, BLACK, ['b', 'c'], possible_moves)
            self.check_castling_possible(board, 'h', 8, BLACK, ['g', 'f', 'e'], possible_moves)
        return possible_moves

    def check_castling_possible(self, board, l, n, color, to_be_empty, possible_moves):
        fields_empty = True
        for letter in to_be_empty:
            if board.get_piece_from_square(letter, n):
                fields_empty = False
        if self.get_color() == color and \
                isinstance(board.get_piece_from_square(l, n), Bishop) and \
                board.get_piece_from_square(l, n).get_color() == color and \
                fields_empty:
            print("Castling possible!")
            possible_moves.append((l, n))
            return True
