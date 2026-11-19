class Solution:
    def knightProbability(self, n, k, row, column):
        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        dp = {(row, column): 1.0}

        for _ in range(k):
            next_dp = {}

            for (r, c), probability in dp.items():
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < n:
                        next_dp[(nr, nc)] = (
                            next_dp.get((nr, nc), 0)
                            + probability / 8
                        )

            dp = next_dp

        return sum(dp.values())