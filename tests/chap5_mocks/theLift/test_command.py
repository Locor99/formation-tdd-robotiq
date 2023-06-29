from unittest import TestCase
from src.chap5_mocks.theLift.command import Command, Request, Call, DIRECTION_ANY, DIRECTION_UP, DIRECTION_DOWN
from src.chap5_mocks.theLift.lift import Lift


class TestCommand(TestCase):
    def test_aCommand_shouldBeSmallerThanAnotherCommand_whenItsFloorIsLower(self):
        self.assertLess(Command(1), Command(2))




class TestCall(TestCase):

    def test_aCall_shouldKnowItsFloor(self):
        call = Call(floor=1, direction= DIRECTION_DOWN)
        self.assertEqual(call.floor(), 1)

    def test_aCall_shouldKnowItsDirection(self):
        call = Call(floor=1, direction= DIRECTION_DOWN)
        self.assertEqual(call.direction(), DIRECTION_DOWN)

    def test_isSameDirectionGoingUp_withCallGoingUp_shouldReturnTrue(self):
        call = Call(0, DIRECTION_UP)
        self.assertTrue(call.isSameDirection(DIRECTION_UP))

    def test_isSameDirectionAny_withCallGoingUp_shouldReturnTrue(self):
        call = Call(0, DIRECTION_UP)
        self.assertTrue(call.isSameDirection(DIRECTION_ANY))

    def test_isSameDirectionGoingDown_withCallGoingUp_shouldReturnFalse(self):
        call = Call(0, DIRECTION_UP)
        self.assertFalse(call.isSameDirection(DIRECTION_DOWN))

    def test_isSameDirectionGoingUp_withCallGoingDown_shouldReturnFalse(self):
        call = Call(0, DIRECTION_DOWN)
        self.assertFalse(call.isSameDirection(DIRECTION_UP))

    def test_isSameDirectionAny_withCallGoingDown_shouldReturnTrue(self):
        call = Call(0, DIRECTION_DOWN)
        self.assertTrue(call.isSameDirection(DIRECTION_ANY))

    def test_isSameDirectionGoingDown_withCallGoingDown_shouldReturnTrue(self):
        call = Call(0, DIRECTION_DOWN)
        self.assertTrue(call.isSameDirection(DIRECTION_DOWN))

    def test_isSameDirection_withAnyRequest_shouldReturnTrue(self):
        request = Request(0)
        self.assertTrue(request.isSameDirection(DIRECTION_UP))
        self.assertTrue(request.isSameDirection(DIRECTION_DOWN))
        self.assertTrue(request.isSameDirection(DIRECTION_ANY))

    def test_twoCalls_shouldBeEqual_whenFloorAndDirectionIsEqual(self):
        self.assertEqual(Call(1, DIRECTION_DOWN),
                         Call(1, DIRECTION_DOWN))

        self.assertNotEqual(Call(1, DIRECTION_DOWN),
                            Call(2, DIRECTION_DOWN))

        self.assertNotEqual(Call(1, DIRECTION_DOWN),
                            Call(1, DIRECTION_UP))


class TestRequest(TestCall):
    def test_aRequest_shouldKnowItsFloor(self):
        request = Request(floor=1)
        self.assertEqual(request.floor(), 1)

    def test_twoRequests_shouldBeEqual_whenFloorIsEqual(self):
        self.assertEqual(Request(1),
                         Request(1))

        self.assertNotEqual(Request(1),
                            Request(2))