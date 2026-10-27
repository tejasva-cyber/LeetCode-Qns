class Solution:
    def checkRecord(self, n):
        MOD = 10**9 + 7
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1

        for _ in range(n):
            ndp = [[0] * 3 for _ in range(2)]

            for a in range(2):
                for l in range(3):
                    val = dp[a][l]
                    ndp[a][0] = (ndp[a][0] + val) % MOD

                    if a == 0:
                        ndp[1][0] = (ndp[1][0] + val) % MOD

                    if l < 2:
                        ndp[a][l + 1] = (ndp[a][l + 1] + val) % MOD

            dp = ndp

        return sum(sum(row) for row in dp) % MOD