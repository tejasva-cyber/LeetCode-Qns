import random
import collections

class RandomizedCollection(object):
    def __init__(self):
        self.nums = []
        self.pos = collections.defaultdict(set)

    def insert(self, val):
        # A value is considered 'new' if its set of indices is empty prior to insertion
        is_new = len(self.pos[val]) == 0
        
        self.pos[val].add(len(self.nums))
        self.nums.append(val)
        
        return is_new

    def remove(self, val):
        # State validation: Ensure value exists and has active indices
        if not self.pos[val]:
            return False

        # 1. Retrieve the target index and the tail state
        remove_idx = self.pos[val].pop()
        last_val = self.nums[-1]
        last_idx = len(self.nums) - 1

        # 2. O(1) Memory Overwrite: Swap target with the tail if it's not already the tail
        if remove_idx != last_idx:
            self.nums[remove_idx] = last_val
            self.pos[last_val].remove(last_idx)
            self.pos[last_val].add(remove_idx)

        # 3. Clean up the tail
        self.nums.pop()

        # 4. Prune empty memory states to maintain hash integrity
        if not self.pos[val]:
            del self.pos[val]

        return True

    def getRandom(self):
        return random.choice(self.nums)