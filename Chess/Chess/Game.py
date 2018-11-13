import itertools
from Board import Board
from Piece import Piece, King, Pawn, Queen
from utils import WHITE, BLACK, choose_field


class Game:

    def __init__(self) -> None:
        self.players = self.initialize_players()
        self.board = Board()
        self.current_player = self.players[1]
        self.turn_number = 1

    def get_board(self):
        return self.board

    def run(self):
        self.initialize_starting_board()
        king_killed = False
        while not king_killed:
            field_chosen, destination = None, None
            self.show_board()
            current_player = self.get_current_player()

            valid_piece_chosen = False
            while not valid_piece_chosen:
                print(f"{current_player.get_name()}'s move. Choose a piece to move")
                field_chosen = current_player.choose_a_piece_to_move()
                valid_piece_chosen = self.get_board().validate_piece_choice(field_chosen, current_player)
                if valid_piece_chosen:
                    piece_chosen = self.get_board().get_piece_from_square(field_chosen[0], field_chosen[1])
                    print("You chose to move: " + str(piece_chosen) + " from " + str(field_chosen))
                    possible_moves = self.get_possible_moves(piece_chosen, field_chosen)
                    if not possible_moves:
                        print("You cannot move this piece!")
                        valid_piece_chosen = False
                    else:
                        print("Possible moves: " + str(possible_moves))

            valid_destination_chosen = False
            while not valid_destination_chosen:
                destination = current_player.choose_a_destination()
                if destination in possible_moves:
                    valid_destination_chosen = True
            king_killed, color_loosing = self.get_board().check_is_king_alive(destination)
            self.get_board().execute_move(field_chosen, destination, piece_chosen)
            self.check_both_mates(destination)
            self.check_promotion()
        self.show_board()
        for player in self.players:
            if player.get_color() == color_loosing:
                looser = player
        print(f"{looser.get_name()}'s king was killed, {looser} lost the game!")

    def check_promotion(self):
        for line in self.get_board().board:
            for square in (line[0], line[-1]):
                piece = square.get_piece()
                if square.get_number() == '8' and isinstance(piece, Pawn) and piece.get_color() == WHITE:
                    square.set_square_free()
                    self.get_board().set_piece_on_square(square.get_letter(), square.get_number(), Queen(WHITE))
                elif square.number == '1' and isinstance(piece, Pawn) and piece.get_color() == BLACK:
                    square.set_square_free()
                    self.get_board().set_piece_on_square(square.get_letter(), square.get_number(), Queen(BLACK))

    def check_both_mates(self, destination):
        defending_king_location, defending_king = None, None
        future_piece_chosen = self.get_board().get_piece_from_square(destination[0], destination[1])
        color_attacking = future_piece_chosen.get_color()
        color_defending = BLACK if color_attacking == WHITE else WHITE
        for line in self.get_board().board:
            for square in line:
                piece = square.get_piece()
                if piece and piece.get_color() == color_defending and isinstance(piece, King):
                    defending_king = piece
                    defending_king_location = (square.letter, int(square.number))
                    print(defending_king_location)
                    break
        attacking_moves = set()
        for line in self.get_board().board:
            for square in line:
                piece = square.get_piece()
                if piece and piece.get_color() == color_attacking:
                    field = (square.letter, square.number)
                    possible_move_set = set(self.get_possible_moves(piece, field))
                    attacking_moves.update(possible_move_set)
        print(attacking_moves)
        if defending_king_location in attacking_moves:
            runaway_moves = set(self.get_possible_moves(defending_king, defending_king_location))
            print(runaway_moves)
            if runaway_moves.issubset(attacking_moves):
                print("Stallmate!")
            else:
                print("Checkmate!")

    def get_possible_moves(self, piece_chosen, field_chosen):
        assert isinstance(piece_chosen, Piece)
        board = self.get_board()
        return piece_chosen.get_possible_moves(field_chosen, board)

    def initialize_starting_board(self):
        self.board.initialize_starting_board()

    def initialize_players(self):
        # name = input(("Welcome to the chess game.\nWhat's the name of 1st player?\n"))
        name = "walter"
        player1 = Player(name, WHITE)
        # name = input("What's the name of 2nd player?\n")
        name = "betty"
        player2 = Player(name, BLACK)
        print(
            f"{player1.get_name()} is {player1.get_color()} and {player2.get_name()} is {player2.get_color()}. Let's begin!\n")
        return player1, player2

    def get_current_player(self):
        id = 1 if self.current_player.get_id() == 0 else 0
        self.current_player = self.players[id]
        return self.current_player

    def show_board(self):
        print(self.board)


class Player:
    newid = itertools.count()

    def __init__(self, name, color) -> None:
        self.id = next(Player.newid)
        self.name = name
        self.color = color

    def __repr__(self) -> str:
        return str(self.id) + " " + self.name + " " + self.color

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def choose_a_piece_to_move(self):
        return choose_field("Choose a piece to move:\n")

    def choose_a_destination(self):
        return choose_field("Where do you want to move?\n")
