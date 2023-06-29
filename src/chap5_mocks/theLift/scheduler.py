from src.chap5_mocks.theLift.command import Request, Call
class Scheduler:

    def __init__(self):
        self._calls = []

    def add_call(self, floor, direction):
        self._calls.append(Call(floor, direction))

    def getCalls(self):
        return self._calls

    def next(self):
        return self._calls.pop(0)
