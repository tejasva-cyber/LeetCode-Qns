import random
import collections

# Architecture 1: The O(1) Time Indexer (Recommended for Heavy Query Loads)
class Solution(object):
    def __init__(self, nums):
        # Pre-compute the memory map during initialization
        self.indices = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target):
        # O(1) Time Execution
        return random.choice(self.indices[target])


# Architecture 2: Your Original Reservoir Sampling (Sanitized)
class SolutionReservoir(object):
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        # O(N) Time, O(1) Space Execution
        result = -1
        count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randrange(count) == 0:
                    result = i
        return result