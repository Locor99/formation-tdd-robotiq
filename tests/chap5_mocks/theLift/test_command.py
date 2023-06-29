from unittest import TestCase
from src.chap5_mocks.theLift.command import Command, Request, Call
from src.chap5_mocks.theLift.lift import Lift


class TestCommand(TestCase):
    def test_aCommand_shouldBeSmallerThanAnotherCommand_whenItsFloorIsLower(self):
        self.assertLess(Command(1), Command(2))


class TestCall(TestCase):

    def test_aCall_shouldKnowItsFloor(self):
        call = Call(floor=1, direction=Lift.DIRECTION_DOWN)
        self.assertEqual(call.floor(), 1)

    def test_aCall_shouldKnowItsDirection(self):
        call = Call(floor=1, direction=Lift.DIRECTION_DOWN)
        self.assertEqual(call.direction(), Lift.DIRECTION_DOWN)

    def test_twoCalls_shouldBeEqual_whenFloorAndDirectionIsEqual(self):
        self.assertEqual(Call(1, Lift.DIRECTION_DOWN),
                         Call(1, Lift.DIRECTION_DOWN))

        self.assertNotEqual(Call(1, Lift.DIRECTION_DOWN),
                            Call(2, Lift.DIRECTION_DOWN))

        self.assertNotEqual(Call(1, Lift.DIRECTION_DOWN),
                            Call(1, Lift.DIRECTION_UP))


class TestRequest(TestCall):
    def test_aRequest_shouldKnowItsFloor(self):
        request = Request(floor=1)
        self.assertEqual(request.floor(), 1)

    def test_twoRequests_shouldBeEqual_whenFloorIsEqual(self):
        self.assertEqual(Request(1),
                         Request(1))

        self.assertNotEqual(Request(1),
                            Request(2))