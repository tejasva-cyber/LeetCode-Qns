class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        n = len(nums)

        half = (n + 1) // 2
        small = nums[:half][::-1]
        large = nums[half:][::-1]

        nums[::2] = small
        nums[1::2] = large