import unittest

from src.chap1_functions.tic_tac_toe import tic_tac_toe

class MyTestCase(unittest.TestCase):
    def test_reaching_3_SHOULD_say_tic_instead(self):
        expected = "1 2 tic 4"
        received = tic_tac_toe(4)
        self.assertEqual(received, expected)

    def test_reaching_5_SHOULD_say_tac_instead(self):
        expected = "1 2 tic 4 tac"
        received = tic_tac_toe(5)
        self.assertEqual(received, expected)

    def test_reaching_a_multiple_of_15_SHOULD_say_tictac(self):
        expected = "1 2 tic 4 tac tic 7 8 tic tac 11 tic 13 14 tictac"
        received = tic_tac_toe(15)
        self.assertEqual(received, expected)

    def test_providing_toe_SHOULD_say_toe_when_a_multiple_is_reached(self):
        toe = 2
        expected = "1 toe"

        received = tic_tac_toe(toe=toe, target=2)

        self.assertEqual(received, expected)

    def test_SHOULD_say_tic_tac_or_toe_WHENEVER_a_multiple_is_reached(self):
        toe = 5 # Don't care if same as tic or tac
        expected = "1 2 tic 4 tactoe tic 7 8 tic tactoe 11 tic 13 14 tictactoe"

        received = tic_tac_toe(15, toe)

        self.assertEqual(received, expected)
