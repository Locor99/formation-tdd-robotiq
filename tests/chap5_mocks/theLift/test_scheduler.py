from unittest import TestCase
from src.chap5_mocks.theLift.scheduler import Scheduler
from src.chap5_mocks.theLift.lift import Lift
from src.chap5_mocks.theLift.command import DIRECTION_ANY, DIRECTION_UP, DIRECTION_DOWN


class TestScheduler(TestCase):
    def setUp(self) -> None:
        self.scheduler = Scheduler()

    # def test_scheduler_shouldRemember_addedCalls(self):
    #     self.scheduler.add_call(1, Lift.DIRECTION_UP)
    #     self.scheduler.add_call(2, Lift.DIRECTION_DOWN)
    #
    #     self.assertEqual(self.scheduler.commands(),
    #                      [Call(1, Lift.DIRECTION_UP), Call(2, Lift.DIRECTION_DOWN)])

    def test_next_withoutCommands_shouldReturnNoFloor(self):
        NO_FLOOR = None
        self.assertEqual(self.scheduler.next(0, DIRECTION_ANY), NO_FLOOR)
        self.assertEqual(self.scheduler.next(0, DIRECTION_UP), NO_FLOOR)
        self.assertEqual(self.scheduler.next(0, DIRECTION_DOWN), NO_FLOOR)

    def test_next_withOneCall_shouldReturnTheCalledFloor(self):
        self.scheduler.add_call(floor=1, direction=DIRECTION_UP)
        self.assertEqual(self.scheduler.next(0, DIRECTION_UP), 1)

    def test_next_withOneRequest_shouldReturnTheRequestedFloor(self):
        self.scheduler.add_request(floor=1)
        self.assertEqual(self.scheduler.next(0, DIRECTION_UP), 1)

    def test_nextGoingUp_withManyAboveCallsGoingUp_shouldReturnClosestFloor(self):
        actualFloor = 0
        self.scheduler.add_call(floor=2, direction=DIRECTION_UP)
        self.scheduler.add_call(floor=1, direction=DIRECTION_UP)

        self.assertEqual(self.scheduler.next(actualFloor, DIRECTION_UP), 1)

    def test_nextGoingUp_withAboveCallsMultipleDirections_shouldReturnClosestOfSameDirection(self):
        actualFloor = 0
        self.scheduler.add_call(floor=1, direction=DIRECTION_DOWN)
        self.scheduler.add_call(floor=2, direction=DIRECTION_UP)

        self.assertEqual(self.scheduler.next(actualFloor, DIRECTION_UP), 2)

    def test_nextGoingUp_withAboveCallsGoingDown_shouldReturnFurthestFloor(self):
        actualFloor = 0
        self.scheduler.add_call(floor=1, direction=DIRECTION_DOWN)
        self.scheduler.add_call(floor=2, direction=DIRECTION_DOWN)

        self.assertEqual(self.scheduler.next(actualFloor, DIRECTION_UP), 2)

    def test_nextGoingDown_withManyBelowCallsGoingDown_shouldReturnClosestFloor(self):
        actualFloor = 5
        self.scheduler.add_call(floor=2, direction=DIRECTION_DOWN)
        self.scheduler.add_call(floor=3, direction=DIRECTION_DOWN)

        self.assertEqual(self.scheduler.next(actualFloor, DIRECTION_DOWN), 3)

    def test_nextGoingDown_withBelowCallsMultipleDirections_shouldReturnClosestOfSameDirection(self):
        actualFloor = 5
        self.scheduler.add_call(floor=1, direction=DIRECTION_DOWN)
        self.scheduler.add_call(floor=2, direction=DIRECTION_UP)

        self.assertEqual(self.scheduler.next(actualFloor, DIRECTION_DOWN), 1)

    def test_nextGoingDown_withBelowCallsGoingUp_shouldReturnFurthestFloor(self):
        actualFloor = 5
        self.scheduler.add_call(floor=4, direction=DIRECTION_UP)
        self.scheduler.add_call(floor=3, direction=DIRECTION_UP)

        self.assertEqual(self.scheduler.next(actualFloor, DIRECTION_DOWN), 3)

    def test_nextGoingUp_withManyAboveRequests_shouldReturnClosestFloor(self):
        actualFloor = 0
        self.scheduler.add_request(floor=2)
        self.scheduler.add_request(floor=1)

        self.assertEqual(self.scheduler.next(actualFloor, DIRECTION_UP), 1)

    def test_nextGoingDown_withAboveRequests_shouldReturnClosestFloor(self):
        actualFloor = 5
        self.scheduler.add_request(floor=2)
        self.scheduler.add_request(floor=1)

        self.assertEqual(self.scheduler.next(actualFloor, DIRECTION_DOWN), 2)
