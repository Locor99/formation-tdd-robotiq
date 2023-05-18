from src.chap5_mocks.accumulator import Accumulator

import sys


class Maximum(Accumulator):
    def __init__(self):
        self._maximum = sys.float_info.min

    def accumulate(self, value):
        self._maximum = max(self._maximum, value)

    def extract(self):
        extracted = self._maximum
        self._maximum = sys.float_info.min
        return extracted

