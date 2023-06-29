from src.chap5_mocks.theLift.command import DIRECTION_UP, DIRECTION_DOWN, DIRECTION_ANY

MAX_LIFT_FLOORS = 1000
class Lift:

    def __init__(self):
        self._floor = 0
        self._direction = DIRECTION_ANY
        self._isWaitingForARequest = False
        self._calls = []

    def call(self, callingFloor, direction):
        if self._isWaitingForARequest:
            self._calls.append(callingFloor)

        else:
            self._floor = callingFloor
            self._isWaitingForARequest = True

    def request(self, targetFloor):
        self._floor = targetFloor
        self._isWaitingForARequest = False
        if self._calls:
            self._floor = self._calls.pop(0)

    def floor(self):
        return self._floor

    def direction(self):
        return self._direction
