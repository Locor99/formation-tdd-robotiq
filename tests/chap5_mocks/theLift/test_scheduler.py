from unittest import TestCase
from src.chap5_mocks.theLift.scheduler import Scheduler


class TestScheduler(TestCase):
    def setUp(self) -> None:
        self.scheduler = Scheduler()

    def test_scheduler_shouldRemember_addedCalls(self):
        self.scheduler.add_call(1, Scheduler.DIRECTION_UP)
        self.scheduler.add_call(2, Scheduler.DIRECTION_DOWN)

        self.assertEqual(self.scheduler.getCalls(),
                         [[1, Scheduler.DIRECTION_UP], [2, Scheduler.DIRECTION_DOWN]])

    def test_scheduler_shouldPointNextFloor_whenOneCallWasMade(self):
        self.scheduler.add_call(1, Scheduler.DIRECTION_DOWN)
        self.assertEqual(1, self.scheduler.next())

