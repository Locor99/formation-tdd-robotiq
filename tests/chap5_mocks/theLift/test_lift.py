from unittest import TestCase
from unittest.mock import create_autospec
from src.chap5_mocks.theLift.lift import Lift
from src.chap5_mocks.theLift.scheduler import Scheduler
from src.chap5_mocks.theLift.command import DIRECTION_UP, DIRECTION_DOWN, DIRECTION_ANY


ANY_DIRECTION = DIRECTION_UP


class TestLift(TestCase):
    def setUp(self) -> None:
        self.scheduler = create_autospec(Scheduler)
        self.lift = Lift(self.scheduler)

    def test_callingLift_shouldUseSchedulerToGoToNextFloor(self):
        self.scheduler.next.return_value = 42

        self.lift.call(42, ANY_DIRECTION)

        self.scheduler.add_call.assert_called_with(42, ANY_DIRECTION)
        self.scheduler.next.assert_called()
        self.assertEqual(self.lift.floor(), 42)

    def test_aCalledLift_shouldNotMoveBeforeARequestIsMade(self):
        self.scheduler.next.side_effect = [1]

        self.lift.call(1, ANY_DIRECTION)
        self.lift.call(2, ANY_DIRECTION)

        self.scheduler.next.assert_called_once()

    def test_requestingFloor_shouldBringItThere(self):
        self.lift.request(5)
        self.assertEqual(self.lift.floor(), 5)

    def test_callingLift_AfterARequestIsMade_shouldBringItToCallingFloor(self):
        self.lift.call(1, ANY_DIRECTION)
        self.lift.request(2)

        self.lift.call(3, ANY_DIRECTION)

        self.assertEqual(self.lift.floor(), 3)

    def test_aCalledLift_shouldRememberNextCall(self):
        self.lift.call(1, DIRECTION_UP)
        self.lift.call(3, ANY_DIRECTION)

        self.lift.request(2)

        self.assertEqual(self.lift.floor(), 3)

    def test_aCalledLift_crossingAnIntermediateFloorThatCalledForSameDirection_shouldStopAtThisFloor(
        self,
    ):
        self.lift.call(10, ANY_DIRECTION)
        self.lift.call(5, DIRECTION_UP)

        self.lift.request(2)

        self.assertEqual(self.lift.floor(), 5)
