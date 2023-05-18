from unittest import TestCase

from src.chap2_structures.config_interpreter import ConfigInterpreter, Input

CONFIG_FILE = "tests/chap2_structures/test.conf"


class TestConfigInterpreter(TestCase):
    def setUp(self):
        self.interpreter = ConfigInterpreter(CONFIG_FILE)

    def test_exercise1_SHOULD_return_key_and_period_as_tuples_FROM_objects_with_period(self):
        expected = [("publisher",6), ("equipment_0",3.5)]
        received = self.interpreter.exercise1()
        self.assertEqual(received, expected)

    def test_exercise2_SHOULD_return_list_of_inputs_as_objects_FROM_equipment_0(self):
        input1 = Input("good_count", "0", "count")
        input2 = Input("reject_count", "1", "count")
        input3 = Input("is_active", "2", "state")
        expected_inputs = [input1, input2, input3]

        received_inputs = self.interpreter.exercise2()

        self.assertEqual(received_inputs[0].name, expected_inputs[0].name)
        self.assertEqual(received_inputs[0].type, expected_inputs[0].type)
        self.assertEqual(received_inputs[0].input, expected_inputs[0].input)
        self.assertEqual(received_inputs[1].name, expected_inputs[1].name)
        self.assertEqual(received_inputs[1].input, expected_inputs[1].input)
        self.assertEqual(received_inputs[1].type, expected_inputs[1].type)
        self.assertEqual(received_inputs[2].name, expected_inputs[2].name)
        self.assertEqual(received_inputs[2].input, expected_inputs[2].input)
        self.assertEqual(received_inputs[2].type, expected_inputs[2].type)

    def test_exercice3_SHOULD_return_maximum_value_and_its_coordinates_as_tuple_FROM_data_measurements(self):
        expected = ([2, 32], 9000)
        maximum, minimum = self.interpreter.exercise3()
        self.assertEqual(maximum, expected)

    def test_exercice3_SHOULD_return_minimum_value_and_its_coordinates_as_tuple_FROM_data_measurements(self):
        expected = ([7, 61], 665)
        maximum, minimum = self.interpreter.exercise3()
        self.assertEqual(minimum, expected)


