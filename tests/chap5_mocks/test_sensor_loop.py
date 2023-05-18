from unittest import TestCase
from unittest.mock import create_autospec

from queue import Queue

from src.chap5_mocks.accumulator import Accumulator
from src.chap5_mocks.sensor_loop import SensorLoop, GET_VALUE_COMMAND, EXIT_COMMAND, NEW_INPUT_VALUE_COMMAND

NO_REQUEST = True
HAS_REQUEST = False


class TestSensorLoop(TestCase):
    def setUp(self):
        self._accumulator = create_autospec(Accumulator)
        self._events = create_autospec(Queue)
        self._responses = create_autospec(Queue)

        self._sensor_loop = SensorLoop(self._accumulator, self._events, self._responses)

    def test_run_SHOULD_stop_running_ON_exit_command_received(self):
        self._events.get.return_value = (EXIT_COMMAND,)

        self._sensor_loop.run()

    def test_run_SHOULD_refresh_accumulator_ON_new_input_event(self):
        expected_input = 42
        self._events.get.side_effect = [(NEW_INPUT_VALUE_COMMAND, expected_input), (EXIT_COMMAND,)]

        self._sensor_loop.run()

        self._accumulator.accumulate.assert_called_with(expected_input)

    def test_run_SHOULD_send_extracted_response_ON_get_value_command_received(self):
        expected = 42
        self._events.get.side_effect = [(GET_VALUE_COMMAND,), (EXIT_COMMAND,)]
        self._accumulator.extract.return_value = expected

        self._sensor_loop.run()

        self._responses.put.assert_called_with(expected)


