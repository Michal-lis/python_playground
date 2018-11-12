from Game import Game
from utils import ask_if_again
import sys

"""
QUESTIONS:
1.self.so_sth ma samo to robic operujac na self.board czy prowadzic do self.board.do_sth? czy moze self.get_board().metoda? 
np. self.get_board().execute_move(piece_chosen, destination) - czy to nie wyglada dziwnie?
2. jak uniknac local variable might be referenced before assignment?

Conclusions:
When you build your class with good interface and good data structures the rest is very fast
"""


def main():
    cmdlineargs = sys.argv
    if cmdlineargs[1] in ['-h', '-help']:
        with open("instruction.txt", 'r') as file:
            instruction = file.read()
            print(instruction)

    again = False
    while not again:
        chess_game = Game()
        chess_game.run()
        again = ask_if_again()
    print("Thank you for playing!")


if __name__ == '__main__':
    main()
