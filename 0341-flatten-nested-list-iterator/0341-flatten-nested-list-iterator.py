class NestedIterator:
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self):
        self._flatten()
        return self.stack.pop().getInteger()

    def hasNext(self):
        self._flatten()
        return len(self.stack) > 0

    def _flatten(self):
        while self.stack and not self.stack[-1].isInteger():
            nested = self.stack.pop().getList()
            self.stack.extend(nested[::-1])