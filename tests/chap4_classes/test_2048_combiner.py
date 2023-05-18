from unittest import TestCase
from src.chap4_classes.combiner import Combiner


class TestCombiner(TestCase):
    def test_an_empty_array_should_be_squashed_into_an_empty_array(self):
        aCombiner = Combiner()
        array = [None, None, None, None]
        squashedArray = aCombiner.squash(array)

        self.assertEqual([None, None, None, None], squashedArray)

    def test_an_array_with_one_element_on_the_right_should_be_squashed_into_an_array_with_the_element_on_the_left(self):
        aCombiner = Combiner()
        array = [None, None, None, 2]
        squashedArray = aCombiner.squash(array)

        self.assertEqual([2, None, None, None], squashedArray)