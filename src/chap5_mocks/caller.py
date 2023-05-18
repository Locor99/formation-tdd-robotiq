class Caller:
    def __init__(self, callee):
        self.callee = callee

    def make_some_calls(self):
        self.callee.method("hello")
        self.callee.method("world")
        self.callee.other_method("!")
