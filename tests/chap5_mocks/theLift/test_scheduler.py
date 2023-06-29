from unittest import TestCase
from src.chap5_mocks.theLift.scheduler import Scheduler
from src.chap5_mocks.theLift.lift import Lift
from src.chap5_mocks.theLift.command import Request, Call


class TestScheduler(TestCase):
    def setUp(self) -> None:
        self.scheduler = Scheduler()

    def test_scheduler_shouldRemember_addedCalls(self):
        self.scheduler.add_call(1, Lift.DIRECTION_UP)
        self.scheduler.add_call(2, Lift.DIRECTION_DOWN)

        # self.assertEqual(self.scheduler.getCalls(),
        #                  [Call(1, Lift.DIRECTION_UP), Call(2, Lift.DIRECTION_DOWN)])

    # def test_scheduler_shouldPointNextFloor_whenOneCallWasMade(self):
    #     self.scheduler.add_call(1, Lift.DIRECTION_DOWN)
    #     self.assertEqual(1, self.scheduler.next())

