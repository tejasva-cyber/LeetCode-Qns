import random
from itertools import accumulate
from bisect import bisect_left

class Solution:
    def __init__(self, w):
        self.prefix = list(accumulate(w))
        self.total = self.prefix[-1]

    def pickIndex(self):
        target = random.randint(1, self.total)
        return bisect_left(self.prefix, target)