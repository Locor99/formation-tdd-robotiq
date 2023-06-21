from unittest import TestCase
from src.chap5_mocks.theLift.lift import Lift


class TestLift(TestCase):
    def setUp(self) -> None:
        self.aLift = Lift(0)

    def test_aCall_shouldMoveTheLiftToTargetFloor(self):
        targetFloor = 5
        self.aLift.moveLiftToTargetFloor(targetFloor)
        self.assertEqual(self.aLift.getFloor(), targetFloor)

    def test_direction_shouldBeUp_whenCallingFromUpperFloor(self):
        self.aLift.moveLiftToTargetFloor(5)
        self.assertEqual(self.aLift.getDirection(), Lift._DIRECTION_UP)

    def test_direction_shouldBeDown_whenCallingFromLowerFloor(self):
        self.aLift.moveLiftToTargetFloor(5)
        self.aLift.moveLiftToTargetFloor(0)
        self.assertEqual(self.aLift.getDirection(), Lift._DIRECTION_DOWN)

    # def test_theLift_shouldGoToTargetFloor_OnlyIfDirectionIsNulOrTowardsTargetFloor(self):
    #     self.aLift.moveLiftToTargetFloor(5)

