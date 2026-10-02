from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        rows, cols = len(matrix), len(matrix[0])

        if rows > cols:
            matrix = list(map(list, zip(*matrix)))
            rows, cols = cols, rows

        ans = float('-inf')

        for top in range(rows):
            sums = [0] * cols

            for bottom in range(top, rows):
                for c in range(cols):
                    sums[c] += matrix[bottom][c]

                prefix = [0]
                cur = 0

                for x in sums:
                    cur += x
                    i = bisect_left(prefix, cur - k)

                    if i < len(prefix):
                        ans = max(ans, cur - prefix[i])

                    insort(prefix, cur)

        return ans