class Solution:
    def moveZeroes(self, nums):
        position = 0

        for num in nums:
            if num != 0:
                nums[position] = num
                position += 1

        while position < len(nums):
            nums[position] = 0
            position += 1