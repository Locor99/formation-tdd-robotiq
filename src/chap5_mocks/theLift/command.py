class Command:
    def __init__(self, floor):
        self._floor = floor

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


class Request(Command):
    def __init__(self, floor):
        super().__init__(floor)
