from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal <= 0:
            return True

        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        @lru_cache(None)
        def win(used, remaining):
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << i

                if not used & bit:
                    if i >= remaining or not win(used | bit, remaining - i):
                        return True

            return False

        return win(0, desiredTotal)