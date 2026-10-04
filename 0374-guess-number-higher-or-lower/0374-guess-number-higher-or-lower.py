# The guess(num) API is provided by LeetCode.

class Solution:
    def guessNumber(self, n):
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result < 0:
                right = mid - 1
            else:
                left = mid + 1