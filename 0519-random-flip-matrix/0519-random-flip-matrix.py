import random

class Solution:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.total = m * n
        self.remaining = self.total
        self.map = {}

    def flip(self):
        r = random.randrange(self.remaining)
        self.remaining -= 1

        x = self.map.get(r, r)
        self.map[r] = self.map.get(self.remaining, self.remaining)

        return [x // self.n, x % self.n]

    def reset(self):
        self.remaining = self.total
        self.map.clear()