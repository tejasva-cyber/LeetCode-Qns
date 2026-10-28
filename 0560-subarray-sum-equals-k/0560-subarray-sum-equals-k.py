from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        total = answer = 0

        for num in nums:
            total += num
            answer += prefix_count[total - k]
            prefix_count[total] += 1

        return answer