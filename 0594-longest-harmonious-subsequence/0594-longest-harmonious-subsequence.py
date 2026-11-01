from collections import Counter

class Solution:
    def findLHS(self, nums):
        count = Counter(nums)
        answer = 0

        for num in count:
            if num + 1 in count:
                answer = max(
                    answer,
                    count[num] + count[num + 1]
                )

        return answer