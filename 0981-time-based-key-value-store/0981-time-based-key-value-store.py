from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key, value, timestamp):
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        values = self.store[key]
        i = bisect_right(values, (timestamp, chr(127))) - 1

        return values[i][1] if i >= 0 else ""