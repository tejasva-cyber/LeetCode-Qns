class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])

        return [i + 1 for i, num in enumerate(nums) if num > 0]