from enum import Enum


class CodeColors(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2
    ORANGE = 3
    PURPLE = 4
    BROWN = 5
    GREY = 6
    PINK = 7
    YELLOW = 8


class CodeFeedback(Enum):
    ABSENT = 0
    WRONG_POSITION = 1
    VALID = 2


class CodeValidator:
    def __init__(self, code_length):
        self._valid_code = []
        self._code_length = code_length

    def setCode(self, code: list):
        self._valid_code = code

    def validateCode(self, submitted_code: list):
        validity = [None for _ in range(self._code_length)]

        for i in range(self._code_length):
            submitted_color = submitted_code[i]
            valid_color = self._valid_code[i]

            if submitted_color is valid_color:
                validity[i] = CodeFeedback.VALID

            elif submitted_color in self._valid_code:
                validity[i] = CodeFeedback.WRONG_POSITION

            else:
                validity[i] = CodeFeedback.ABSENT

        return validity
