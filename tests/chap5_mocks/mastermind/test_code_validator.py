from unittest import TestCase
from src.chap5_mocks.mastermind.code_validator import (
    CodeValidator,
    CodeColors,
    CodeFeedback,
)


class TestCodeValidator(TestCase):
    def setUp(self) -> None:
        self.code_validator = CodeValidator(4)

    def test_submitCode_withFourAbsentColors_shouldReturnAllAbsentStates(self):
        self.code_validator.setCode(
            [CodeColors.GREY, CodeColors.BROWN, CodeColors.YELLOW, CodeColors.RED]
        )

        code_validity = self.code_validator.validateCode(
            [CodeColors.GREEN, CodeColors.BLUE, CodeColors.ORANGE, CodeColors.PINK]
        )

        self.assertEqual(
            code_validity,
            [
                CodeFeedback.ABSENT,
                CodeFeedback.ABSENT,
                CodeFeedback.ABSENT,
                CodeFeedback.ABSENT,
            ],
        )

    def test_submitCode_withAllGoodColors_shouldReturnAllValidState(self):
        self.code_validator.setCode(
            [CodeColors.GREY, CodeColors.BROWN, CodeColors.YELLOW, CodeColors.RED]
        )

        code_validity = self.code_validator.validateCode(
            [CodeColors.GREY, CodeColors.BROWN, CodeColors.YELLOW, CodeColors.RED]
        )

        self.assertEqual(
            code_validity,
            [
                CodeFeedback.VALID,
                CodeFeedback.VALID,
                CodeFeedback.VALID,
                CodeFeedback.VALID,
            ],
        )

    def test_submitCode_withColorAtWrongPosition_shouldReturnWrongPosition(self):
        self.code_validator.setCode(
            [CodeColors.GREEN, CodeColors.BROWN, CodeColors.YELLOW, CodeColors.RED]
        )

        code_validity = self.code_validator.validateCode(
            [CodeColors.BLUE, CodeColors.BLUE, CodeColors.BLUE, CodeColors.YELLOW]
        )

        self.assertEqual(
            code_validity,
            [
                CodeFeedback.ABSENT,
                CodeFeedback.ABSENT,
                CodeFeedback.ABSENT,
                CodeFeedback.WRONG_POSITION,
            ],
        )
