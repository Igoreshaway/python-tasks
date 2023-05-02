class Iterator:
    def __init__(self, string: str):
        self.string = string
        self.index: int = 0

    def iter(self):
        return self

    def next(self):
        if self.index < len(self.string):
            result: str = self.string[self.index]
            self.index += 1
            return result
        raise StopIteration


