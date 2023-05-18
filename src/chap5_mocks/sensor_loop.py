from src.chap5_mocks.accumulator import Accumulator
from src.chap5_mocks.sensor import ARG_INDEX, COMMAND_INDEX, EXIT_COMMAND, GET_VALUE_COMMAND, NEW_INPUT_VALUE_COMMAND

from queue import Queue


class SensorLoop(object):
    def __init__(self, accumulator: Accumulator, events: Queue, responses: Queue):
        self._accumulator = accumulator
        self._events = events
        self._responses = responses

    def run(self):
        while True:
            event = self._events.get()

            if event[COMMAND_INDEX] == NEW_INPUT_VALUE_COMMAND:
                self._accumulator.accumulate(event[ARG_INDEX])

            elif event[COMMAND_INDEX] == GET_VALUE_COMMAND:
                self._responses.put(self._accumulator.extract())

            elif event[COMMAND_INDEX] == EXIT_COMMAND:
                break
