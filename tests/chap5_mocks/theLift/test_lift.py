from unittest import TestCase
from src.chap5_mocks.theLift.lift import Lift


class TestLift(TestCase):
    def test_aCall_shouldMoveTheLiftToActualFloor(self):
        aLift = Lift(0)
        sourceFloor = 5

        aLift.call(sourceFloor)

        self.assertEqual(aLift.getFloor(), sourceFloor)

