import json

CONFIG_FILE = "/usr/local/lib/anymeasure.conf"


class Configuration:
    def __init__(self):
        with open(CONFIG_FILE, 'r') as file:
            self._data = json.loads(file.read())

    def read_configuration_from_json_file(self):
        return self._data
