from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1

        distance = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                        mat[nr][nc] = mat[r][c] + 1
                        queue.append((nr, nc))

        return mat