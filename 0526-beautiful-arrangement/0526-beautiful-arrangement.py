from functools import lru_cache

class Solution:
    def countArrangement(self, n):
        @lru_cache(None)
        def dp(mask):
            pos = mask.bit_count() + 1

            if pos > n:
                return 1

            total = 0

            for num in range(1, n + 1):
                if not (mask & (1 << num)):
                    if num % pos == 0 or pos % num == 0:
                        total += dp(mask | (1 << num))

            return total

        return dp(0)