class Solution:
    def countPalindromicSubsequences(self, s):
        MOD = 10**9 + 7
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1

            for j in range(i + 1, n):
                if s[i] != s[j]:
                    dp[i][j] = (
                        dp[i + 1][j] + dp[i][j - 1]
                        - dp[i + 1][j - 1]
                    ) % MOD
                else:
                    low = i + 1
                    high = j - 1

                    while low <= high and s[low] != s[i]:
                        low += 1

                    while low <= high and s[high] != s[i]:
                        high -= 1

                    inner = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0

                    if low > high:
                        dp[i][j] = 2 * inner + 2
                    elif low == high:
                        dp[i][j] = 2 * inner + 1
                    else:
                        dp[i][j] = 2 * inner - dp[low + 1][high - 1]

                    dp[i][j] %= MOD

        return dp[0][n - 1]