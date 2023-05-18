from unittest import TestCase
import os

from src.chap4_classes.line_compactor import LineCompactor, FileNotFoundException

class TestLineCompactor(TestCase):
    def setUp(self):
        self.from_path = "tests/chap4_classes/origin.txt"
        self.invalid_path = "tests/chap4_classes/missing.txt"
        self.to_path = "tests/chap4_classes/target.txt"
        self.compactor = LineCompactor()

    def test_missing_from_file_SHOULD_raise_exception(self):
        self.assertRaises(FileNotFoundException, self.compactor.compact, self.invalid_path, self.to_path)

    def test_compact_SHOULD_create_file_at_specified_path(self):
        self.compactor.compact(self.from_path, self.to_path)
        self.assertTrue(os.path.isfile(self.to_path))

    def test_compact_SHOULD_compact_all_lines_FROM_origin_file_into_one(self):
        expected = "montypythonflyingcircus"

        self.compactor.compact(self.from_path, self.to_path)

        with open(self.to_path) as file:
            lines = [line.rstrip('\n') for line in file]
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0], expected)





    def tearDown(self):
        if os.path.isfile(self.to_path):
            os.remove(self.to_path)