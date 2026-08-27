class Solution:
    def spiralOrder(self, matrix):
        result = []

        while matrix:
            result += matrix.pop(0)

            for row in matrix:
                if row:
                    result.append(row.pop())

            if matrix:
                result += matrix.pop()[::-1]

            for row in matrix[::-1]:
                if row:
                    result.append(row.pop(0))

        return result