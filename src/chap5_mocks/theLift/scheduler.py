from src.chap5_mocks.theLift.command import Request, Call
from src.chap5_mocks.theLift.lift import Lift
class Scheduler:

    def __init__(self):
        self._commands = []

    def add_call(self, floor, direction):
        self._commands.append(Call(floor, direction))

    def commands(self):
        return self._commands

    def nextTargetFloor(self, actualFloor, actualDirection): #Pas sûr de ça, faut shooter des infos à chaque utilisation
        sortedCommands = self._commands

        if actualDirection is Lift.DIRECTION_UP:
            sortedCommands = list(filter(lambda command: command.floor()>actualFloor, sortedCommands))
            return min(sortedCommands).floor()

        elif actualDirection is Lift.DIRECTION_DOWN:
            sortedCommands = list(filter(lambda command: command.floor() < actualFloor, sortedCommands))
            return max(sortedCommands).floor()






