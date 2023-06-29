class Scheduler:
    DIRECTION_DOWN = -1
    DIRECTION_NONE = 0
    DIRECTION_UP = 1

    def __init__(self):
        self._calls = []

    def add_call(self, floor, direction):
        self._calls.append([floor, direction])

    def getCalls(self):
        return self._calls

    def next(self):
        return self._calls.pop(0)[0]


class Command:
    def __init__(self, floor):
        self._floor = floor


class Call(Command):
    def __init__(self, floor, direction):
        super().__init__(floor)
        self._direction = direction


class Request(Command):
    def __init__(self, floor):
        super().__init__(floor)
