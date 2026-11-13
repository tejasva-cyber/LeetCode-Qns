class Solution:
    def strangePrinter(self, s):
        s = ''.join(c for i, c in enumerate(s) if i == 0 or c != s[i - 1])
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1

            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j] + 1

                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        middle = dp[i + 1][k - 1] if k > i + 1 else 0
                        dp[i][j] = min(
                            dp[i][j],
                            middle + dp[k][j]
                        )

        return dp[0][n - 1]