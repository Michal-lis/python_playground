WHITE = 'white'
BLACK = 'black'
letters_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def convert_l_n_to_indexes(letter, number):
    x_axis = letters_dict[letter]
    y_axis = int(number) - 1
    return x_axis, y_axis
