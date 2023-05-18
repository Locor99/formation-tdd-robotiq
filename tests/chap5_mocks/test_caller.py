from unittest import TestCase
from unittest.mock import MagicMock, ANY, call

from src.chap5_mocks.caller import Caller

class TestCaller(TestCase):
    def setUp(self):
        self.callee = MagicMock()
        self.caller = Caller(self.callee)

    def test_callee_method_SHOULD_be_called_WITH_any_param_AT_LEAST_once(self):
        self.caller.make_some_calls()
        self.callee.method.assert_called()

    def test_callee_method_SHOULD_be_called_WITH_hello(self):
        calls = [call("hello"), call(ANY)]
        self.caller.make_some_calls()
        self.callee.method.assert_has_calls(calls)

    def test_callee_method_SHOULD_be_called_WITH_world(self):
        calls = [call(ANY), call("world")]
        self.caller.make_some_calls()
        self.callee.method.assert_has_calls(calls)

    def test_callee_other_method_SHOULD_be_called_only_once(self):
        self.caller.make_some_calls()
        self.assertEqual(self.callee.other_method.call_count, 1)

    def test_every_calls_SHOULD_be_in_order_EVEN_IF_it_is_bad_to_do_so(self):
        self.caller.make_some_calls()
        self.callee.assert_has_calls([call.method(ANY), call.method(ANY), call.other_method("!")])
