class Scheduler:

    def __init__(self):
        self._calls = []

    def add_call(self, floor, direction):
        self._calls.append([floor, direction])

    def getCalls(self):
        return self._calls

    def next(self):
        return self._calls.pop(0)[0]
