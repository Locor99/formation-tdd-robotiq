from unittest import TestCase

from tests.chap3_scripts.unix_shell import UnixShell, SUCCESS_RETURN_CODE, OUTPUT_INDEX, RETURN_CODE_INDEX

import json

PATH_TO_LIST = " tests/chap3_scripts/files_to_size/"
SCRIPT = "src/chap3_scripts/python_tree.py"


class TestTree(TestCase):
    def setUp(self):
        self.shell = UnixShell()

    def test_calling_script_WITHOUT_path_SHOULD_return_error(self):
        output = self.shell.get_output_from_command(SCRIPT)
        self.assertNotEqual(output[RETURN_CODE_INDEX], SUCCESS_RETURN_CODE)

    def test_calling_script_WITHOUT_path_SHOULD_print_usage(self):
        output = self.shell.get_output_from_command(SCRIPT)
        self.assertEqual(output[OUTPUT_INDEX], "Invalid usage!")

    def test_calling_WITH_path_SHOULD_return_without_error(self):
        output = self.shell.get_output_from_command(SCRIPT + PATH_TO_LIST)
        self.assertEqual(output[RETURN_CODE_INDEX], SUCCESS_RETURN_CODE)

    def test_calling_WITH_path_SHOULD_return_dictionary_of_sizes(self):
        output = self.shell.get_output_from_command(SCRIPT + PATH_TO_LIST)

        tree = json.loads(output[OUTPUT_INDEX])

        self.assertEqual(len(tree.keys()), 3)
        self.assertEqual(tree["once.jpg"], 30133)
        self.assertEqual(tree["ni.jpg"], 23090)
        self.assertEqual(tree["woa.jpg"], 93713)
