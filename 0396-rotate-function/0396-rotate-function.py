class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)

        current = sum(i * nums[i] for i in range(n))
        ans = current

        for k in range(1, n):
            current = current + total - n * nums[-k]
            ans = max(ans, current)

        return ans