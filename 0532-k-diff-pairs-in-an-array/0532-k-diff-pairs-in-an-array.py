from collections import Counter

class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0

        counts = Counter(nums)

        if k == 0:
            return sum(freq > 1 for freq in counts.values())

        return sum(num + k in counts for num in counts)