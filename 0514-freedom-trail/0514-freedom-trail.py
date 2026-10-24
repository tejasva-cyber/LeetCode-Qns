from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring, key):
        n = len(ring)
        positions = {}

        for i, ch in enumerate(ring):
            positions.setdefault(ch, []).append(i)

        @lru_cache(None)
        def dp(pos, idx):
            if idx == len(key):
                return 0

            ans = float('inf')
            for nxt in positions[key[idx]]:
                dist = abs(nxt - pos)
                steps = min(dist, n - dist)
                ans = min(ans, steps + 1 + dp(nxt, idx + 1))

            return ans

        return dp(0, 0)