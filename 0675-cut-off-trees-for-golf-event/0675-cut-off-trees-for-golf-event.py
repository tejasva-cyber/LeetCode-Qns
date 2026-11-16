from collections import deque

class Solution:
    def cutOffTree(self, forest):
        m, n = len(forest), len(forest[0])

        trees = sorted(
            (forest[i][j], i, j)
            for i in range(m)
            for j in range(n)
            if forest[i][j] > 1
        )

        def bfs(sr, sc, tr, tc):
            if (sr, sc) == (tr, tc):
                return 0

            queue = deque([(sr, sc, 0)])
            visited = {(sr, sc)}

            while queue:
                r, c, steps = queue.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < m and 0 <= nc < n
                        and forest[nr][nc] != 0
                        and (nr, nc) not in visited
                    ):
                        if (nr, nc) == (tr, tc):
                            return steps + 1

                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))

            return -1

        total = 0
        sr = sc = 0

        for _, tr, tc in trees:
            steps = bfs(sr, sc, tr, tc)

            if steps == -1:
                return -1

            total += steps
            sr, sc = tr, tc

        return total