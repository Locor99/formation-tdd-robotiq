from src.chap5_mocks.theLift.command import Request, Call, DIRECTION_ANY, DIRECTION_DOWN, DIRECTION_UP
from src.chap5_mocks.theLift.lift import MAX_LIFT_FLOORS

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

            if actualDirection is DIRECTION_UP:
                # minimumDistance = MAX_LIFT_FLOORS
                # for command in self._commands:
                #     distanceActualFloorToCommandFloor = self._calculateDistance(command, actualFloor, actualDirection)
                #     if distanceActualFloorToCommandFloor < minimumDistance:
                #         minimumDistance = distanceActualFloorToCommandFloor
                #         closestFloor = command.floor()
                #
                # return closestFloor
                distances = []
                for command in self._commands:
                    distances.append(self._calculateDistance(command, actualFloor, actualDirection))

                indexOfMinDistance = distances.index(min(distances))
                closestFloor = self._commands[indexOfMinDistance].floor()
                return closestFloor

        else:
            return None

    def _calculateDistance(self, command, actualFloor, actualDirection):
        offset = 0 if command.isSameDirection(actualDirection) else 2*(MAX_LIFT_FLOORS - command.floor())
        return command.floor() - actualFloor + offset
