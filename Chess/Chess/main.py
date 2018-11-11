from Game import Game

"""
QUESTIONS:
1.self.so_sth ma samo to robic operujac na self.board czy prowadzic do self.board.do_sth? czy moze self.get_board().metoda? 
np. self.get_board().execute_move(piece_chosen, destination) - czy to nie wyglada dziwnie?
2. jak uniknac local variable might be referenced before assignment?
"""

def main():
    again = False
    while not again:
        chess_game = Game()
        chess_game.run()
        again = chess_game.ask_if_again()
    print("Thank you for playing!")


if __name__ == '__main__':
    main()
