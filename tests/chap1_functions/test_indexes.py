import unittest
from unittest.mock import patch

from src.chap1_functions.indexes import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.numbers = [42,42,42,42,42,42,42,42,42,42,2,1,3,1,1]
    @patch('src.chap1_functions.indexes.len')
    def test_sum_SHOULD_be_correct_AND_not_use_len(self, mock_len):
        expected_sum = 8
        mock_len.return_value = 0

        total = return_sum_of_last_5_numbers_without_using_len(self.numbers)

        self.assertEqual(total, expected_sum)

    def test_sum_numbers_3_to_10_SHOULD_be_correct(self):
        expected_sum = 294
        total = return_sum_of_numbers_3_to_10(self.numbers)
        self.assertEqual(total, expected_sum)

    @patch('src.chap1_functions.indexes.len')
    def test_part_SHOULD_return_beginning(self, mock_len):
        message= "beginningbeforeend"
        expected = "beginning"
        mock_len.return_value = 0

        received = return_part_of_string_without_using_len(message)

        self.assertEqual(received, expected)

    @patch('src.chap1_functions.indexes.len')
    def test_part_SHOULD_return_end(self, mock_len):
        message = "nothingafterend"
        expected = "end"
        mock_len.return_value = 0

        received = return_part_of_string_without_using_len(message)

        self.assertEqual(received, expected)

    @patch('src.chap1_functions.indexes.len')
    def test_path_SHOULD_return_wholestring(self, mock_len):
        message = "wholestring"
        mock_len.return_value = 0

        received = return_part_of_string_without_using_len(message)

        self.assertEqual(received, message)
