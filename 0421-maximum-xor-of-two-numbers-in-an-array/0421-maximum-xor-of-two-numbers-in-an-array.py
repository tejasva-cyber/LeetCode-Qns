class Solution:
    def findMaximumXOR(self, nums):
        answer = 0
        mask = 0

        for bit in range(31, -1, -1):
            mask |= 1 << bit
            prefixes = {num & mask for num in nums}
            candidate = answer | (1 << bit)

            if any((candidate ^ prefix) in prefixes for prefix in prefixes):
                answer = candidate

        return answer