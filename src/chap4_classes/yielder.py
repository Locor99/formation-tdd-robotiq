class Yielder:
    def __init__(self, input, should_return_True_callback):
        self._input = input
        self._should_return_True_callback = should_return_True_callback

    def provide_doubling_generator(self):
        for i in self._input:
            yield i*2

    def return_true_until_callback_decides_otherwise(self):
        while self._should_return_True_callback():
            yield True
        yield False
