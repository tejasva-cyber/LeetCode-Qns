class Solution:
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        values = [x for row in mat for x in row]
        return [
            values[i * c:(i + 1) * c]
            for i in range(r)
        ]