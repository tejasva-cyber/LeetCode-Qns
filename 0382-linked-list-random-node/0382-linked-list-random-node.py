import random

class Solution:

    def __init__(self, head):
        self.head = head

    def getRandom(self):
        result = None
        node = self.head
        i = 1

        while node:
            if random.randrange(i) == 0:
                result = node.val
            node = node.next
            i += 1

        return result