'''
Make multiple battleships: you'll need to be careful because 
you need to make sure that you don’t place battleships on top 
of each other on the game board. You'll also want to make sure
 that you balance the size of the board with the number of 
 ships so the game is still challenging and fun to play.

Make battleships of different sizes: this is trickier than it 
sounds. All the parts of the battleship need to be vertically 
or horizontally touching and you’ll need to make sure you don’t 
 place part of a ship off the side of the board.

Make your game a two-player game.
'''
from random import randint, shuffle


def init(a):  # tworzy tablice a na a biala
    board = []
    for x in range(0, a):
        board.append(["O"] * a)
    return board


def print_board(b):  # drukuje tablice
    for row in b:
        print("  ".join(row))


def change_board_ship(b, row, col):
    b[row - 1][col - 1] = "#"


def randomise(b, s):  # losuje na planszy b dana liczbe statkow s
    all_fields = [(i, j) for i in range(len(b)) for j in range(len(b))]
    shuffle(all_fields)
    return all_fields[:s]


def get_guess():
    print("C'mon, make a guess!")
    row = int(input("Guess Row:"))
    if type(row)==int:
        col = int(input("Guess Col:"))
        if type(col)==int:
            pass
        else:
            getguess()
    else:
        getguess()
    return row, col

# funkcja gry
board = init(10)
print_board(board)
input("Here is where the game begins. Ready?")
ships = randomise(board, 10)
print("Initializing the ships", end=" ")
for each in ships:
    change_board_ship(board, each[0], each[1])
    print(" .", end=" ")
print(".")
k=0
while(k<10):
    print_board(board)
    guess_row, guess_col = get_guess()
    if board[guess_row-1][guess_col-1]=="#": # to statek który pływa
        print("Congratulations! You sank my battleship")
        board[guess_row-1][guess_col-1]="@" # @ to zatopiony statek
        k=k+1
    else:
        if (guess_row not in range(len(board))) or (guess_col not in range(len(board))):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row-1][guess_col-1] == "X":
            print("You guessed that one already. It was not a ship")
        elif board[guess_row-1][guess_col-1] == "@":
            print("You guessed that one already. It was a ship")
        else:
            print("You missed my battleship!")
            board[guess_row - 1][guess_col - 1] = "X"
print("You win!")




