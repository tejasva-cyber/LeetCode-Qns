from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        self.values = {}
        self.freqs = defaultdict(OrderedDict)

    def _update(self, key):
        freq = self.values[key][1]
        del self.freqs[freq][key]

        if not self.freqs[freq] and self.min_freq == freq:
            self.min_freq += 1

        self.values[key][1] += 1
        new_freq = self.values[key][1]
        self.freqs[new_freq][key] = None

    def get(self, key):
        if key not in self.values:
            return -1

        self._update(key)
        return self.values[key][0]

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.values:
            self.values[key][0] = value
            self._update(key)
            return

        if len(self.values) == self.capacity:
            key_to_remove, _ = self.freqs[self.min_freq].popitem(last=False)
            del self.values[key_to_remove]

        self.values[key] = [value, 1]
        self.freqs[1][key] = None
        self.min_freq = 1