from src.chap5_mocks.theLift.command import DIRECTION_UP, DIRECTION_DOWN, DIRECTION_ANY
from src.chap5_mocks.theLift.scheduler import Scheduler


class Lift:
    def __init__(self, scheduler: Scheduler):
        self._floor = 0
        self._direction = DIRECTION_ANY
        self._isWaitingForARequest = False
        self._calls = []
        self._scheduler = scheduler

    def call(self, callingFloor, direction):
        self._scheduler.add_call(callingFloor, direction)

        if self._isWaitingForARequest:
            self._calls.append(callingFloor)

        else:
            self._floor = self._scheduler.next(self._floor, self._direction)
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
