from unittest import TestCase
from src.chap4_classes.combiner import Combiner


class TestCombiner(TestCase):
    def setUp(self) -> None:
        self.aCombiner = Combiner()

    def test_an_empty_array_should_be_squashed_into_an_empty_array(self):
        squashedArray = self.aCombiner.squash([None, None, None, None])

        self.assertEqual([None, None, None, None], squashedArray)

    def test_an_array_with_one_tile_on_the_right_should_be_squashed_into_an_array_with_the_tile_on_the_left(self):
        squashedArray = self.aCombiner.squash([None, None, None, 2])

        self.assertEqual([2, None, None, None], squashedArray)

    def test_an_array_with_two_different_tiles_not_on_left_side_should_stack_left(self):
        squashedArray = self.aCombiner.squash([None, 4, None, 2])

        self.assertEqual([4, 2, None, None], squashedArray)
    # Ce test passe déjà. Le comportement existait déjà.
    # Je garderais le test, car il apporte un autre niveau de complexité...?

    def test_an_array_with_two_tiles_of_same_value_should_add_up_and_stack_left(self):
        squashedArray = self.aCombiner.squash([None, 2, None, 2])

        self.assertEqual([4, None, None, None], squashedArray)