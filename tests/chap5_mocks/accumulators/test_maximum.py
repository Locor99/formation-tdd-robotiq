from unittest import TestCase

import sys

from src.chap5_mocks.accumulators.maximum import Maximum

delta = 0.0001


class TestMaximum(TestCase):
    def setUp(self):
        self._accumulator = Maximum()

    def test_no_read_SHOULD_extract_negative_infinite_float(self):
        expected = sys.float_info.min
        received = self._accumulator.extract()
        self.assertAlmostEqual(received, expected, delta=delta)

    def test_one_read_SHOULD_extract_that_number(self):
        expected = 42
        self._accumulator.accumulate(expected)

        received = self._accumulator.extract()

        self.assertAlmostEqual(received, expected, delta=delta)

    def test_accumulate_many_value_SHOULD_return_max(self):
        expected = 42

        self._accumulator.accumulate(expected)
        self._accumulator.accumulate(expected / 2)

        received = self._accumulator.extract()
        self.assertAlmostEqual(received, expected, delta=delta)

    def test_extract_WHEN_values_accumulated_SHOULD_flush_read_values(self):
        expected = sys.float_info.min
        self._accumulator.accumulate(42)

        self._accumulator.extract()

        received = self._accumulator.extract()
        self.assertAlmostEqual(received, expected, delta=delta)
