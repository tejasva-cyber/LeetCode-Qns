class Solution:
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1

        while left < len(nums) and nums[left] == sorted_nums[left]:
            left += 1

        while right > left and nums[right] == sorted_nums[right]:
            right -= 1

        return right - left + 1 if left < right else 0