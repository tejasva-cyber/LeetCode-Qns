from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes):
        n = len(boxes)

        @lru_cache(None)
        def dp(left, right, extra):
            if left > right:
                return 0

            while left < right and boxes[right] == boxes[right - 1]:
                right -= 1
                extra += 1

            result = dp(left, right - 1, 0) + (extra + 1) ** 2

            for i in range(left, right):
                if boxes[i] == boxes[right]:
                    result = max(
                        result,
                        dp(left, i, extra + 1)
                        + dp(i + 1, right - 1, 0)
                    )

            return result

        return dp(0, n - 1, 0)