from unittest import TestCase
from src.chap5_mocks.theLift.command import Command, Request, Call
from src.chap5_mocks.theLift.lift import Lift


class TestCall(TestCase):

    def test_aCall_shouldKnowItsFloor(self):
        call = Call(floor=1, direction=Lift.DIRECTION_DOWN)
        self.assertEqual(call.getFloor(), 1)

    def test_aCall_shouldKnowItsDirection(self):
        call = Call(floor=1, direction=Lift.DIRECTION_DOWN)
        self.assertEqual(call.getDirection(), Lift.DIRECTION_DOWN)

    def test_twoCalls_shouldBeComparable(self):
        self.assertEqual(Call(1, Lift.DIRECTION_DOWN),
                         Call(1, Lift.DIRECTION_DOWN))

        self.assertNotEqual(Call(1, Lift.DIRECTION_DOWN),
                            Call(2, Lift.DIRECTION_DOWN))

        self.assertNotEqual(Call(1, Lift.DIRECTION_DOWN),
                            Call(1, Lift.DIRECTION_UP))


class TestRequest(TestCall):
    def test_aRequest_shouldKnowItsFloor(self):
        request = Request(floor=1)
        self.assertEqual(request.getFloor(), 1)

    def test_twoRequests_shouldBeComparable(self):
        self.assertEqual(Request(1),
                         Request(1))

        self.assertNotEqual(Request(1),
                            Request(2))

