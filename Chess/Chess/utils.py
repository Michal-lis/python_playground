WHITE = 'white'
BLACK = 'black'
letters_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
reverse_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def convert_l_n_to_indexes(letter, number):
    x_axis = letters_dict[letter]
    y_axis = int(number) - 1
    return x_axis, y_axis


def choose_field(text):
    valid_input = False
    while not valid_input:
        chosen_field = input(text)
        if len(chosen_field) != 2:
            print("Please give an input as: 'xy' where x is a letter and y is a number")
            continue
        letter_from = chosen_field[0]
        number_from = chosen_field[1]
        try:
            number_from = int(number_from)
        except ValueError:
            print("Please make the second sign a number from 1 to 8")
            continue
        if letter_from not in letters or number_from not in numbers:
            print("Please make the first sign a number from 'a' to 'h'")
            continue
        return letter_from.lower(), int(number_from)


def convert_indexes_to_l_n(idx, idy):
    letter = reverse_dict[idx]
    number = idy + 1
    return letter, number


def ask_if_again():
    correct_input = False
    while not correct_input:
        answer = input("\nDo you want to play again?\nPlease answer 'yes' or 'no'.")
        if answer == "yes":
            return False
        elif answer == "no":
            return True


def is_within_board(x, y):
    return True if (0 <= x <= 7) and (0 <= y <= 7) else False
