from unittest import TestCase
from unittest.mock import ANY, patch

import json

from src.chap5_mocks.configuration import Configuration, CONFIG_FILE

class TestConfiguration(TestCase):
    def setUp(self):
        self._loaded_configuration = {
            "topic1": {
                "meaningOfLife": 42
            },
            "topic2": {
                "lifeOf": 3.14159
            }
        }

    @patch("src.chap5_mocks.configuration.open")
    def test_new_configuration_SHOULD_load_json_FROM_default_filename(self, open_mock):
        self._given_a_file_with_content(open_mock)
        Configuration()
        open_mock.assert_called_with(CONFIG_FILE, ANY)

    @patch("src.chap5_mocks.configuration.open")
    def test_loaded_configuration_SHOULD_contain_all_keys_FROM_configuration_file(self, open_mock):
        self._given_a_file_with_content(open_mock)
        config = Configuration()

        data = config.read_configuration_from_json_file()

        for key in self._loaded_configuration:
            self.assertTrue(key in data.keys())

    def _given_a_file_with_content(self, open_mock):
        file = open_mock.return_value.__enter__.return_value
        file.read.return_value = json.dumps(self._loaded_configuration)
