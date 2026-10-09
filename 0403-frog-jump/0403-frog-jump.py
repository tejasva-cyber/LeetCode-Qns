class Solution:
    def canCross(self, stones):
        positions = set(stones)
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for stone in stones:
            for jump in dp[stone]:
                for next_jump in (jump - 1, jump, jump + 1):
                    if next_jump > 0 and stone + next_jump in positions:
                        dp[stone + next_jump].add(next_jump)

        return bool(dp[stones[-1]])