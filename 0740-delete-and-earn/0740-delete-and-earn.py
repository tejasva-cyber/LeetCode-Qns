from collections import Counter

class Solution:
    def deleteAndEarn(self, nums):
        count = Counter(nums)
        points = [0] * (max(nums) + 1)

        for num, frequency in count.items():
            points[num] = num * frequency

        prev2 = prev1 = 0

        for value in points:
            current = max(prev1, prev2 + value)
            prev2, prev1 = prev1, current

        return prev1