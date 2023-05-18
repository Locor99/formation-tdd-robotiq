import unittest

from src.chap1_functions.farg_args_kwargs import *

class MyTestCase(unittest.TestCase):
    def test_mean_WITH_fargs_SHOULD_be_computed_correctly(self):
        expected_mean = 2
        mean = mean_fargs(1, 2, 3)
        self.assertEqual(mean, expected_mean)

    def test_mean_with_linear_args_SHOULD_be_computed_correctly(self):
        expected_mean = 3
        mean = mean_largs(1, 2, 3, 4, 5)
        self.assertEqual(mean, expected_mean)

        args = (1, 2, 3, 4, 5)
        mean_with_largs = mean_largs(*args)
        self.assertEqual(mean_with_largs, expected_mean)

    def test_mean_with_keyword_args_SHOULD_be_computed_correctly(self):
        expected_mean = 4
        mean = mean_kwargs(arg1=3, arg2=4, arg3=5)
        self.assertEqual(mean, expected_mean)

        kwargs = {"arg1": 3, "arg2": 4, "arg3": 5}
        mean_with_kwargs = mean_kwargs(**kwargs)
        self.assertEqual(mean_with_kwargs, expected_mean)

    def test_SHOULD_use_callback_WITH_fargs(self):
        expected = self._callback_fargs(1, 2, 3)
        received = use_callback_with_arg_1_2_3_as_formal_arguments(self._callback_fargs)
        self.assertEqual(received, expected)

    def test_SHOULD_use_callback_WITH_largs(self):
        args = (1, 2, 3)
        expected = self._callback_largs(*args)

        received = use_callback_with_arg_1_2_3_as_linear_arguments(self._callback_largs)

        self.assertEqual(received, expected)

    def test_SHOULD_use_callback_WITH_kwargs(self):
        kwargs = {"any": 42, "bob": 10}
        expected = self._callback_kwargs(**kwargs)

        received = use_callback_with_keyword_arguments_containing_bob_key(self._callback_kwargs, kwargs["bob"])

        self.assertEqual(received, expected)

    def _callback_fargs(self, arg1, arg2, arg3):
        return 192 + arg1 + arg2 - arg3

    def _callback_largs(self, *args):
        sum = 0
        for arg in args:
            sum += arg

        return 42 + sum

    def _callback_kwargs(self, **kwargs):
        if "bob" in kwargs:
            return 9000
        else:
            return 42
