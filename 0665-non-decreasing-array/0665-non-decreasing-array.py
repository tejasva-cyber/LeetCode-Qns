class Solution:
    def checkPossibility(self, nums):
        changes = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                changes += 1

                if changes > 1:
                    return False

                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

        return True