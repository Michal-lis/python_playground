import itertools
import random
import time

sign_x = " X "
sign_o = " 0 "
sign_empty = "   "


def get_user_choice(self):
    return (input("# Make your move! [1-9] : "))

class TicTacToe:
    def __init__(self):
        board = Board()
        self.board = board
        self.player1 = Player()
        self.player2 = Player()
        self.current_player_id = 1
        self.turn_number = 1

    def get_players_name(self):
        name1 = input(("Welcome to the tic-tac-toe game.\nWhat's the name of the player?\n"))
        self.player1 = Player(name1, sign_o)
        self.player2 = Player("Computer", sign_x)
        print(f"Player {self.player1.name} is {self.player1.sign} and {self.player2.name} is {self.player2.sign}.")

    def check_turn_number(self):
        self.turn_number += 1
        if self.turn_number == 10:
            print("It's a draw!")
            return True

    def change_current_player(self):
        if self.current_player_id == 1:
            self.current_player_id = 0
        else:
            self.current_player_id = 1

    def get_current_player(self):
        if self.current_player_id == 1:
            return self.player1
        else:
            return self.player2

    def set_square_sign(self, field_num, sign):
        for square in self.board.squares:
            if square.id == field_num:
                square.sign = sign

    def get_possible_moves(self):
        return [x.id for x in self.board.squares if x.sign == sign_empty]

    def check_winner(self):
        x_list, o_list = [], []
        winning_sets = [(1, 4, 7), (2, 5, 8), (3, 6, 9)] + [(1, 2, 3), (4, 5, 6), (7, 8, 9)] + [(1, 5, 9), (3, 5, 7)]
        for square in self.board.squares:
            if square.sign == sign_x:
                x_list.append(square.id)
            elif square.sign == sign_o:
                o_list.append(square.id)
        x_set = set(x_list)
        o_set = set(o_list)
        for s in winning_sets:
            if set(s).issubset(x_set):
                print("Computer is the winner!")
                return True
            elif set(s).issubset(o_set):
                print("Player is the winner!")
                return True

        return False

    def run_game(self):
        self.get_players_name()
        finished = False
        print(self.board)
        while finished != True:
            current_player = self.get_current_player()
            print(f"{current_player.name}'s move")
            possible_moves = self.get_possible_moves()
            field_chosen = current_player.choose_field(possible_moves)
            self.set_square_sign(field_chosen, current_player.sign)
            finished = self.check_winner() or self.check_turn_number()
            print(self.board)
            self.change_current_player()

    def ask_if_again(self):
        correct_input = False
        while not correct_input:
            answer = input("\nDo you want to play again?\nPlease answer 'yes' or 'no'.")
            if answer == "yes":
                return False
            elif answer == "no":
                return True


class Board:
    __vertical_line = "\n" + 12 * "-" + "\n"

    def __init__(self):
        self.squares = [Square(x + 1, sign_empty) for x in range(9)]

    def __repr__(self):
        return self.squares

    def __str__(self):
        board_str = ""
        for idx, square in enumerate(self.squares):
            if idx in (3, 6):
                board_str += Board.__vertical_line
            board_str += "|" + square.sign + "|"
        return board_str


class Square:
    def __init__(self, id, sign):
        self.id = id
        self.sign = sign


class Player:
    newid = itertools.count()

    def __init__(self, name="", sign=""):
        self.id = next(Player.newid)
        self.name = name
        self.sign = sign

    def get_user_choice(self):
        return (input("# Make your move! [1-9] : "))

    def choose_field(self, possible_moves):
        if self.name == "Computer":
            time.sleep(2)
            return random.choice(possible_moves)
        else:
            correct_input = False
            while not correct_input:
                choice = self.get_user_choice()
                try:
                    choice = int(choice)
                    if choice > 9:
                        print("Your number is too big!")
                    elif choice < 1:
                        print("Your number is too small!")
                    elif choice not in possible_moves:
                        print("This field is already occupied!")
                    else:
                        correct_input = True
                except ValueError:
                    print("Please type an integer value from 1 to 9.")
            return choice


def main():
    again = False
    while not again:
        game = TicTacToe()
        game.run_game()
        again = game.ask_if_again()
    print("Thank you for playing!")


if __name__ == '__main__':
    main()
