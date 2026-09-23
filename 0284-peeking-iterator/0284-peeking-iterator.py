# Iterator is already defined for you.

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked = None

        if self.iterator.hasNext():
            self.peeked = self.iterator.next()

    def peek(self):
        return self.peeked

    def next(self):
        value = self.peeked

        if self.iterator.hasNext():
            self.peeked = self.iterator.next()
        else:
            self.peeked = None

        return value

    def hasNext(self):
        return self.peeked is not None