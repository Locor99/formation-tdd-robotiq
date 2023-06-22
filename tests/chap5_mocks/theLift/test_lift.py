from unittest import TestCase
from src.chap5_mocks.theLift.lift import Lift

ANY_DIRECTION = Lift.DIRECTION_UP
class TestLift(TestCase):

    def setUp(self) -> None:
        self.lift = Lift()

    def test_callingLift_shouldBringItToCallingFloor(self):
        self.lift.call(42, ANY_DIRECTION)
        self.assertEqual(self.lift.floor(), 42)

    def test_requestingFloor_shouldBringItThere(self):
        self.lift.request(5)
        self.assertEqual(self.lift.floor(), 5)

    def test_aCalledLift_shouldNotMoveBeforeARequestIsMade(self):
        self.lift.call(1, ANY_DIRECTION)
        self.lift.call(2, ANY_DIRECTION)
        self.assertEqual(self.lift.floor(), 1)

    def test_callingLift_AfterARequestIsMade_shouldBringItToCallingFloor(self):
        self.lift.call(1, ANY_DIRECTION)
        self.lift.request(2)

        self.lift.call(3, ANY_DIRECTION)

        self.assertEqual(self.lift.floor(), 3)

    def test_aCalledLift_shouldRememberNextCall(self):
        self.lift.call(1, Lift.DIRECTION_UP)
        self.lift.call(3, ANY_DIRECTION)

        self.lift.request(2)

        self.assertEqual(self.lift.floor(), 3)


