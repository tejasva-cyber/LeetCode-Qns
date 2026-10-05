import random

class RandomizedSet(object):
    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val):
        # Active validation: Reject duplicate payloads instantly
        if val in self.pos:
            return False
            
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.pos:
            return False

        # 1. Retrieve the target index and the tail state
        remove_idx = self.pos[val]
        last_val = self.nums[-1]

        # 2. O(1) Memory Overwrite: Point the last value to the removed index
        self.nums[remove_idx] = last_val
        self.pos[last_val] = remove_idx

        # 3. Execute the memory truncation
        self.nums.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        return random.choice(self.nums)