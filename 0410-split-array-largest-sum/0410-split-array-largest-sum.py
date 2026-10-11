class Solution:
    def splitArray(self, nums, k):
        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2
            groups = 1
            current = 0

            for num in nums:
                if current + num > mid:
                    groups += 1
                    current = num
                else:
                    current += num

            if groups > k:
                left = mid + 1
            else:
                right = mid

        return left