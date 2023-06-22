class Scheduler:
    DIRECTION_DOWN = -1
    DIRECTION_NONE = 0
    DIRECTION_UP = 1

    def __init__(self):
        self._calls = []
    def add_call(self, floor):
        self._calls.append(floor)

    def calls(self):
        return self._calls
