import random

class Solution(object):
    def __init__(self, n, blacklist):
        self.bound = n - len(blacklist)
        self.remap = {}

        # Record blacklisted values already sitting in the tail [bound, n - 1]
        tail_black = set()
        for b in blacklist:
            if b >= self.bound:
                tail_black.add(b)

        # Remap every blacklisted slot below bound to a clean slot in the tail
        w = self.bound
        for b in blacklist:
            if b < self.bound:
                while w in tail_black:
                    w += 1
                self.remap[b] = w
                w += 1

    def pick(self):
        r = random.randrange(self.bound)
        return self.remap.get(r, r)