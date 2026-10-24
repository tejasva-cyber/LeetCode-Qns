class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            prev = 0

            for j in range(i + 1, n):
                temp = dp[j]

                if s[i] == s[j]:
                    dp[j] = prev + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])

                prev = temp

        return dp[-1] if s else 0