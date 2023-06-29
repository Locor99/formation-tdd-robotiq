class Command:
    def __init__(self, floor):
        self._floor = floor

    def getFloor(self):
        return self._floor


class Call(Command):
    def __init__(self, floor, direction):
        super().__init__(floor)
        self._direction = direction

    def getDirection(self):
        return self._direction


class Request(Command):
    def __init__(self, floor):
        super().__init__(floor)
