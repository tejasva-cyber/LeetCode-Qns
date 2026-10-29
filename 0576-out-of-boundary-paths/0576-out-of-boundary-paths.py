class Solution:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        answer = 0

        for _ in range(maxMove):
            next_dp = [[0] * n for _ in range(m)]

            for r in range(m):
                for c in range(n):
                    if dp[r][c] == 0:
                        continue

                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < m and 0 <= nc < n:
                            next_dp[nr][nc] = (
                                next_dp[nr][nc] + dp[r][c]
                            ) % MOD
                        else:
                            answer = (answer + dp[r][c]) % MOD

            dp = next_dp

        return answer