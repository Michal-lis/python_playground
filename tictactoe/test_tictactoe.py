import unittest
from tic_tac_toe import TicTacToe, Board, Player, Square, sign_o, sign_empty, sign_x
from unittest.mock import patch


class TestPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    # it is run once only and it is too costly to run these every time e.g. populating a database

    @classmethod
    def tearDownClass(cls):
        # clean what happened in SetUp Class
        print("tearDownClass")

    def setUp(self):
        self.player = Player("Mike", sign_x)
        self.player2 = Player("Computer", sign_o)

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.player.name, "Mike")
        self.assertIsInstance(self.player.id, int)
        self.assertEqual(self.player.sign, sign_x)

        self.assertEqual(self.player2.name, "Computer")
        self.assertIsInstance(self.player2.id, int)
        self.assertEqual(self.player2.sign, sign_o)

    def test_choose_field_computer(self):
        possible_moves = range(10)
        result = self.player2.choose_field(possible_moves=possible_moves)
        self.assertTrue(0 <= result <= 9)
        self.assertIsInstance(result, int)

    @patch('tic_tac_toe.player.get_user_choice', return_value='5')
    def test_choose_field_player(self):
        possible_moves = range(10)
        result = self.player.choose_field(possible_moves=possible_moves)
        self.assertTrue(0 <= result <= 9)
        self.assertIsInstance(result, int)


class TestTictactoe(unittest.TestCase):

    def setUp(self):
        self.player = Player("Mike", sign_x)
        self.player2 = Player("Computer", sign_o)

    def tearDown(self):
        pass

    def test_get_players_name(self):
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
