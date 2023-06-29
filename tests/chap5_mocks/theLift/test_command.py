from unittest import TestCase
from src.chap5_mocks.theLift.command import Command, Request, Call
from src.chap5_mocks.theLift.lift import Lift

class TestCommand(TestCase):
    def test_aRequest_shouldKnowItsFloor(self):
        request = Request(floor=1)
        self.assertEqual(request.getFloor(), 1)

    def test_aCall_shouldKnowItsFloor(self):
        call = Call(floor=1, direction=Lift.DIRECTION_DOWN)
        self.assertEqual(call.getFloor(), 1)

    def test_aCall_shouldKnowItsDirection(self):
        call = Call(floor=1, direction=Lift.DIRECTION_DOWN)
        self.assertEqual(call.getDirection(), Lift.DIRECTION_DOWN)
