from src.chap5_mocks.theLift.command import (
    Request,
    Call,
    DIRECTION_ANY,
    DIRECTION_DOWN,
    DIRECTION_UP,
)

MAX_LIFT_FLOORS = 1000


class Scheduler:
    def __init__(self):
        self._commands = []

    def add_call(self, floor, direction):
        self._commands.append(Call(floor, direction))

    def add_request(self, floor):
        self._commands.append(Request(floor))

    def next(self, actualFloor, actualDirection):
        if self._commands:
            closestFloor = None

            distances = []
            for command in self._commands:
                distances.append(
                    self._calculateDistance(command, actualFloor, actualDirection)
                )

            indexOfMinDistance = distances.index(min(distances))
            closestFloor = self._commands[indexOfMinDistance].floor()
            return closestFloor

        else:
            return None

    def _calculateDistance(self, command, actualFloor, actualDirection):
        if command.isSameDirection(actualDirection):
            distance = abs(actualFloor - command.floor())
        else:
            if actualDirection is DIRECTION_UP:
                distance = 2 * MAX_LIFT_FLOORS - actualFloor - command.floor()

            elif actualDirection is DIRECTION_DOWN:
                distance = actualFloor + command.floor()

        return distance
