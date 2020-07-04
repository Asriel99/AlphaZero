
"""Class to run unit tests for the TicTacToeGame class."""
from unittest import TestCase

from tic_tac_toe.tic_tac_toe_game import TicTacToeGame


class TestTicTacToeGame(TestCase):
    """Class to run unit tests for the TicTacToeGame class."""

    def test_check_game_over_1(self):
        """Test case for the check_game_over function.

        Test for game over with a win.
        """
        game = TicTacToeGame()
        game.state = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
        game_over, value = game.check_game_over(1)

        self.assertEqual(game_over, True)
        self.assertEqual(value, 1)

    def test_check_game_over_2(self):
        """Test case for the check_game_over function.

        Test for game over with a loss.
        """
        game = TicTacToeGame()
        game.state = [[1, 0, -1], [1, 1, 0], [1, -1, -1]]
        game_over, value = game.check_game_over(-1)

        self.assertEqual(game_over, True)
        self.assertEqual(value, -1)

    def test_check_game_over_3(self):
        """Test case for the check_game_over function.

        Test for game over with a draw.
        """
        game = TicTacToeGame()
        game.state = [[1, 1, -1], [-1, -1, 1], [1, 1, -1]]
        game_over, value = game.check_game_over(1)

        self.assertEqual(game_over, True)
        self.assertEqual(value, 0)

    def test_check_game_over_4(self):
        """Test case for the check_game_over function.

        Test for game not over.
        """
        game = TicTacToeGame()
        game.state = [[-1, 0, 0], [0, -1, 0], [0, 1, 0]]
        game_over, value = game.check_game_over(-1)

        self.assertEqual(game_over, False)
        self.assertEqual(value, 0)
