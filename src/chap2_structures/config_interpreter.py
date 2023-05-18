import json
import sys


class ConfigInterpreter:
    def __init__(self, filename: str):
        with open(filename, 'r') as file:
            self._config = json.loads(file.read())

    def exercise1(self):
        period_key = "period"
        periods = []

        for key in self._config.keys():
            if period_key in self._config[key].keys():
                periods.append((key, self._config[key][period_key]))

        return periods

    def exercise2(self):
        inputs = list()

        for input_data in self._config["equipment_0"]["inputs"]:
            inputs.append(Input(input_data["name"], input_data["input"], input_data["type"]))

        return inputs

    def exercise3(self):
        min = sys.maxsize
        min_index = -1
        max = -sys.maxsize - 1
        max_index = -1
        data_key = "data_measurements"

        values = self._config[data_key]["values"]

        for i in range(len(values) - 1):
            if values[i] < min:
                min_index = i
                min = values[i]

            if values[i] > max:
                max_index = i
                max = values[i]

        return (self._config[data_key]["triggers"][max_index], max),\
               (self._config[data_key]["triggers"][min_index], min)

class Input:
    def __init__(self, name, input, type):
        self.name = name
        self.input = input
        self.type = type
