import abc


class Accumulator(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def accumulate(cls, value):
        pass

    @classmethod
    @abc.abstractmethod
    def extract(cls):
        pass
