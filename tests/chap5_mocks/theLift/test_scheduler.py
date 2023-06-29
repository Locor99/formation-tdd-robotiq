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

        self.assertEqual(self.scheduler.commands(),
                         [Call(1, Lift.DIRECTION_UP), Call(2, Lift.DIRECTION_DOWN)])

    def test_scheduler_shouldPointNextTargetFloor_whenOneCallIsMade(self):
        self.scheduler.add_call(floor=1, direction=Lift.DIRECTION_DOWN)
        self.assertEqual(1, self.scheduler.nextTargetFloor(0, Lift.DIRECTION_UP))

    def test_scheduler_shouldPointNextTargetFloorInTrajectory_whenMultipleCallsWereMadeInSameDirection(self):
        actualFloor = 0

        self.scheduler.add_call(floor=2, direction=Lift.DIRECTION_UP)
        self.scheduler.add_call(floor=1, direction=Lift.DIRECTION_UP)

        self.assertEqual(1, self.scheduler.nextTargetFloor(actualFloor, Lift.DIRECTION_UP))

    def test_scheduler_shouldPointNextTargetFloorDown_whenMultipleCallsWereMadeInSameDirection(self):
        actualFloor = 5

        self.scheduler.add_call(floor=1, direction=Lift.DIRECTION_DOWN)
        self.scheduler.add_call(floor=4, direction=Lift.DIRECTION_DOWN)

        self.assertEqual(4, self.scheduler.nextTargetFloor(actualFloor, Lift.DIRECTION_DOWN))

