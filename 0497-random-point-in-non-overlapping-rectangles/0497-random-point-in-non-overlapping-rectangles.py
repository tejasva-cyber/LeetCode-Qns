import random
import bisect

class Solution:
    def __init__(self, rects):
        self.rects = rects
        self.prefix = []
        total = 0

        for x1, y1, x2, y2 in rects:
            total += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.prefix.append(total)

        self.total = total

    def pick(self):
        k = random.randint(1, self.total)
        i = bisect.bisect_left(self.prefix, k)
        x1, y1, x2, y2 = self.rects[i]
        offset = k - (self.prefix[i - 1] if i else 0) - 1
        width = x2 - x1 + 1

        return [x1 + offset % width, y1 + offset // width]