class Lift:
    DIRECTION_NONE = 0
    DIRECTION_UP = 1
    DIRECTION_DOWN = 2

    def __init__(self):
        self._floor = 0
        self._direction = Lift.DIRECTION_NONE
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
