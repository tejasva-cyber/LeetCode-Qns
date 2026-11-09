class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)

        duplicate = sum(nums) - sum(set(nums))
        missing = expected - (actual - duplicate)

        return [duplicate, missing]