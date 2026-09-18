class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        dp = [0] * (cols + 1)
        maximum = 0

        for i in range(1, rows + 1):
            prev = 0

            for j in range(1, cols + 1):
                temp = dp[j]

                if matrix[i - 1][j - 1] == "1":
                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
                    maximum = max(maximum, dp[j])
                else:
                    dp[j] = 0

                prev = temp

        return maximum * maximum