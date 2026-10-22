class Solution:
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []

        for s in range(m + n - 1):
            diagonal = []

            for i in range(max(0, s - n + 1), min(m, s + 1)):
                j = s - i
                diagonal.append(mat[i][j])

            if s % 2 == 0:
                diagonal.reverse()

            result.extend(diagonal)

        return result