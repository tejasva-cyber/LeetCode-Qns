class Solution:
    def numDistinct(self, s, t):
        dp = [0] * (len(t) + 1)
        dp[0] = 1

        for char in s:
            for j in range(len(t), 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[-1]