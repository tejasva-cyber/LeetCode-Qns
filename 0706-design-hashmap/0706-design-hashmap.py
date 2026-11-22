class MyHashMap(object):
    # Unique sentinel objects prevent collisions with valid integer keys (including 0)
    _EMPTY = object()
    _TOMBSTONE = object()

    def __init__(self):
        self.capacity = 256
        self.mask = self.capacity - 1
        self.size = 0
        self.tombstones = 0
        # Parallel contiguous arrays for cache-friendly probing
        self.keys = [self._EMPTY] * self.capacity
        self.vals = [None] * self.capacity

    def _hash(self, key):
        # 32-bit avalanche mixer to eliminate primary clustering on sequential keys
        h = ((key ^ (key >> 16)) * 0x45d9f3b) & 0xFFFFFFFF
        h = ((h ^ (h >> 16)) * 0x45d9f3b) & 0xFFFFFFFF
        return (h ^ (h >> 16)) & self.mask

    def _rehash(self):
        old_keys = self.keys
        old_vals = self.vals

        # Grow only if active entries justify doubling;
        # otherwise compact in-place to purge tombstones without RAM bloat.
        if self.size * 2 >= self.capacity:
            self.capacity <<= 1
            self.mask = self.capacity - 1

        self.keys = [self._EMPTY] * self.capacity
        self.vals = [None] * self.capacity
        self.tombstones = 0

        for i in range(len(old_keys)):
            k = old_keys[i]
            if k is not self._EMPTY and k is not self._TOMBSTONE:
                idx = self._hash(k)
                while self.keys[idx] is not self._EMPTY:
                    idx = (idx + 1) & self.mask
                self.keys[idx] = k
                self.vals[idx] = old_vals[i]

    def put(self, key, value):
        idx = self._hash(key)
        first_tombstone = -1

        while self.keys[idx] is not self._EMPTY:
            if self.keys[idx] == key:
                self.vals[idx] = value
                return
            if self.keys[idx] is self._TOMBSTONE and first_tombstone == -1:
                first_tombstone = idx
            idx = (idx + 1) & self.mask

        if first_tombstone != -1:
            target = first_tombstone
            self.tombstones -= 1
        else:
            target = idx

        self.keys[target] = key
        self.vals[target] = value
        self.size += 1

        # Rehash or compact once active entries + tombstones reach 60% capacity
        if (self.size + self.tombstones) * 10 >= self.capacity * 6:
            self._rehash()

    def get(self, key):
        idx = self._hash(key)
        while self.keys[idx] is not self._EMPTY:
            if self.keys[idx] == key:
                return self.vals[idx]
            idx = (idx + 1) & self.mask
        return -1

    def remove(self, key):
        idx = self._hash(key)
        while self.keys[idx] is not self._EMPTY:
            if self.keys[idx] == key:
                self.keys[idx] = self._TOMBSTONE
                # Scrub value reference immediately to prevent dangling data retention
                self.vals[idx] = None
                self.size -= 1
                self.tombstones += 1
                return
            idx = (idx + 1) & self.mask