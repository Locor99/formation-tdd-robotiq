DIRECTION_DOWN = -1
DIRECTION_ANY = 0
DIRECTION_UP = 1
class Command:
    def __init__(self, floor):
        self._floor = floor

    def isSameDirection(self, direction):
        pass

    def floor(self):
        return self._floor

    def __eq__(self, other):
        return self._floor == other._floor

    def __lt__(self, other):
        return self._floor < other._floor


class Call(Command):
    def __init__(self, floor, direction):
        super().__init__(floor)
        self._direction = direction

    def direction(self):
        return self._direction

    def __eq__(self, other):
        return self._floor == other._floor and\
            self._direction == other._direction

    def isSameDirection(self, direction):
        return direction == self._direction or direction == DIRECTION_ANY

class Request(Command):
    def __init__(self, floor):
        super().__init__(floor)

    def isSameDirection(self, direction):
        return True
