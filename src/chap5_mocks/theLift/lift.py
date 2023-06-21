class Lift:
    _DIRECTION_UP = "up"
    _DIRECTION_DOWN = "down"
    _DIRECTION_NONE = None
    def __init__(self, initialFloor):
        self._floor = initialFloor
        self._direction = None

    def moveLiftToTargetFloor(self, targetFloor):
        if targetFloor > self._floor:
            self._direction = self._DIRECTION_UP
        elif targetFloor < self._floor:
            self._direction = self._DIRECTION_DOWN
        else:
            self._direction = self._DIRECTION_NONE

        self._floor = targetFloor

    def getFloor(self):
        return self._floor

    def getDirection(self):
        return self._direction
