from unittest import TestCase
from src.chap4_classes.combiner import Combiner


class TestCombiner(TestCase):
    def test_an_empty_array_should_be_squashed_in_an_empty_array(self):
        aCombiner = Combiner()
        array = [None, None, None, None]
        squashedArray = aCombiner.squash(array)

        expectedSquashedArray = [None, None, None, None]
        self.assertEqual(expectedSquashedArray, squashedArray)
