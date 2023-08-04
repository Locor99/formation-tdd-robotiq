from unittest import TestCase
from unittest.mock import create_autospec
from src.chap5_mocks.mastermind.code_breaker_chain import CodeBreakerChain

AN_ATTEMPT = [0, 0, 0, 0]


class StubCodeBreakerNode(CodeBreakerChain):
    def __init__(self, attempts, next_node):
        super().__init__(attempts, next_node)
        self.current_node_can_make_an_attempt = True
        self.attempted = False

    def _current_node_can_make_an_attempt(self):
        return self.current_node_can_make_an_attempt

    def _make_an_attempt(self):
        self.attempted = True
        return AN_ATTEMPT


class TestCodeBreakerChain(TestCase):
    def setUp(self) -> None:
        self.attempts = []
        self.next_node = create_autospec(CodeBreakerChain)
        self.chain = StubCodeBreakerNode(self.attempts, self.next_node)

    def test_nodeShouldMakeAnAttempt_whenItCan(self):
        self.chain.current_node_can_make_an_attempt = True
        self.chain.make_an_attempt()
        self.assertTrue(self.chain.attempted)

    def test_nextNodeShouldBeUsed_whenCannotMakeAnAttempt(self):
        self.chain.current_node_can_make_an_attempt = False

        self.chain.make_an_attempt()

        self.assertFalse(self.chain.attempted)
        self.next_node.make_an_attempt.assert_called()
