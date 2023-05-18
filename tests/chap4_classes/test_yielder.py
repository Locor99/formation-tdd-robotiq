from unittest import TestCase

from src.chap4_classes.yielder import Yielder


class TestYielder(TestCase):
    def setUp(self):
        self.input = [1, 2, 3, 4, 5]
        self.yielder = Yielder(self.input, self._callback)
        self.true_countdown = 2

    def test_yield_SHOULD_double_every_input(self):
        i = 0
        for received in self.yielder.provide_doubling_generator():
            self.assertEqual(received, self.input[i] * 2)
            i += 1

    def test_calling_generator_SHOULD_restart_traversal(self):
        i = 0
        for received in self.yielder.provide_doubling_generator():
            self.assertEqual(received, self.input[0] * 2)
            break

        for received in self.yielder.provide_doubling_generator():
            self.assertEqual(received, self.input[i] * 2)
            i += 1

    def test_generator_WITH_callback_SHOULD_return_true_until_countdown_reaches_zero(self):
        expected_number_of_trues = self.true_countdown
        counter = 0

        for received in self.yielder.return_true_until_callback_decides_otherwise():
            if received is True:
                counter += 1


        self.assertEqual(counter, expected_number_of_trues)

    def _callback(self):
        self.true_countdown -= 1
        return self.true_countdown >= 0

