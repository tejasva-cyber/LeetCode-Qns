class Solution:
    def findKthNumber(self, m, n, k):
        left, right = 1, m * n

        while left < right:
            mid = (left + right) // 2
            count = sum(min(mid // i, n) for i in range(1, m + 1))

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left