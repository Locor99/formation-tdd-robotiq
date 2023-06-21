class Lift:
    def __init__(self, initialFloor):
        self._floor = initialFloor

    def call(self, targetFloor):
        self._floor = targetFloor

    def getFloor(self):
        return self._floor
