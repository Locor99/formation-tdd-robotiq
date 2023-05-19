from unittest import TestCase
from src.chap4_classes.combiner import Combiner


class TestCombiner(TestCase):
    def setUp(self) -> None:
        self.aCombiner = Combiner()

    def test_squashAnEmptyArray_ShouldReturnAnEmptyArray(self):
        self._assertThatArraySquashesInto([None, None, None, None],
                                          [None, None, None, None])

    def test_alreadySquashedArray_shouldBeReturnedAsIs(self):
        self._assertThatArraySquashesInto([2, None, None, None],
                                          [2, None, None, None])

    def test_squashWithOneEmptyNeighbor_shouldMoveTileToTheLeft(self):
        self._assertThatArraySquashesInto([None, 2, None, None],
                                          [2, None, None, None])

    def test_squash_shouldMoveTileThroughAllEmptyNeighbors(self):
        self._assertThatArraySquashesInto([None, None, None, 2],
                                          [2, None, None, None])

    def test_twoIdenticalTiles_shouldCombine(self):
        self._assertThatArraySquashesInto([2, 2, None, None],
                                          [4, None, None, None])

    def test_twoDifferentNumbers_shouldStackButNotCombine(self):
        self._assertThatArraySquashesInto([4, None, 2, None],
                                          [4, 2, None, None])

    def test_twoIdenticalTiles_separatedByEmptyNeighbors_shouldCombine(self):
        self._assertThatArraySquashesInto([None, 2, None, 2],
                                          [4, None, None, None])

    def test_manyIdenticalTiles_shouldCombineFromTheLeft(self):
        self._assertThatArraySquashesInto([2, 2, 2, None],
                                          [4, 2, None, None])

    def test_tiles_ShouldNotCombineMoreThanOnce(self):
        self._assertThatArraySquashesInto([4, 2, 2, None],
                                          [4, 4, None, None])

    def test_fullArrayOfTiles_ShouldMergeOnlyOnceDuringSquash(self):
        self._assertThatArraySquashesInto([4, 2, 2, 2],
                                          [4, 4, 2, None])

    def _assertThatArraySquashesInto(self, fromArray, toArray):
        squashedArray = self.aCombiner.squash(fromArray)
        self.assertEqual(toArray, squashedArray)
