class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        NEG = -10**9

        dp = [[NEG] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for step in range(1, 2 * n - 1):
            next_dp = [[NEG] * n for _ in range(n)]

            for r1 in range(max(0, step - n + 1), min(n, step + 1)):
                c1 = step - r1

                if grid[r1][c1] == -1:
                    continue

                for r2 in range(max(0, step - n + 1), min(n, step + 1)):
                    c2 = step - r2

                    if grid[r2][c2] == -1:
                        continue

                    best = max(
                        dp[r1][r2],
                        dp[r1 - 1][r2] if r1 > 0 else NEG,
                        dp[r1][r2 - 1] if r2 > 0 else NEG,
                        dp[r1 - 1][r2 - 1] if r1 > 0 and r2 > 0 else NEG
                    )

                    if best == NEG:
                        continue

                    cherries = grid[r1][c1]

                    if r1 != r2:
                        cherries += grid[r2][c2]

                    next_dp[r1][r2] = best + cherries

            dp = next_dp

        return max(0, dp[n - 1][n - 1])