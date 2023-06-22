from unittest import TestCase
from src.chap5_mocks.theLift.scheduler import Scheduler


class TestScheduler(TestCase):
    def setUp(self) -> None:
        self.scheduler = Scheduler()

    def test_callingLift_shouldBringItToCallingFloor(self):
        self.lift.call(42, ANY_DIRECTION)
        self.assertEqual(self.lift.floor(), 42)

    # def test_scheduler_shouldRemember_addedCalls(self):
    #     self.scheduler.add_call(1)
    #     self.scheduler.add_call(2)
    #     self.scheduler.add_call(3)
    #
    #     self.assertEqual(self.scheduler.calls(), [1, 2, 3])
