class MyHashSet(object):
    def __init__(self):
        self.capacity = 1024
        self.mask = self.capacity - 1
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        # 32-bit avalanche mixing to eliminate clustering on strided inputs
        h = ((key ^ (key >> 16)) * 0x45d9f3b) & 0xFFFFFFFF
        h = ((h ^ (h >> 16)) * 0x45d9f3b) & 0xFFFFFFFF
        return (h ^ (h >> 16)) & self.mask

    def _rehash(self):
        old_buckets = self.buckets
        self.capacity <<= 1
        self.mask = self.capacity - 1
        new_buckets = [[] for _ in range(self.capacity)]

        for bucket in old_buckets:
            for k in bucket:
                new_buckets[self._hash(k)].append(k)

        self.buckets = new_buckets

    def add(self, key):
        bucket = self.buckets[self._hash(key)]
        for k in bucket:
            if k == key:
                return

        bucket.append(key)
        self.size += 1

        # Trigger resize once load factor reaches 0.75
        if self.size * 4 >= self.capacity * 3:
            self._rehash()

    def remove(self, key):
        bucket = self.buckets[self._hash(key)]
        for i in range(len(bucket)):
            if bucket[i] == key:
                # Swap-and-pop achieves O(1) deletion inside the bucket
                bucket[i] = bucket[-1]
                bucket.pop()
                self.size -= 1
                return

    def contains(self, key):
        bucket = self.buckets[self._hash(key)]
        for k in bucket:
            if k == key:
                return True
        return False