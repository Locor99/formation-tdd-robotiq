from abc import ABC, abstractmethod


class CodeBreakerChain(ABC):
    def __init__(self, attempts, next_node):
        self._next_node = next_node
        self._attempts = attempts

    @abstractmethod
    def _make_an_attempt(self):
        pass

    @abstractmethod
    def _current_node_can_make_an_attempt(self):
        pass

    def make_an_attempt(self):
        if self._current_node_can_make_an_attempt():
            self._make_an_attempt()
        else:
            self._next_node.make_an_attempt()
