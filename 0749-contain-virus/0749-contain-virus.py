class Solution:
    def containVirus(self, isInfected):
        m, n = len(isInfected), len(isInfected[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        total_walls = 0

        while True:
            regions = []
            frontiers = []
            walls = []

            visited = [[False] * n for _ in range(m)]

            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1 and not visited[r][c]:
                        region = []
                        frontier = set()
                        wall_count = 0
                        stack = [(r, c)]
                        visited[r][c] = True

                        while stack:
                            x, y = stack.pop()
                            region.append((x, y))

                            for dx, dy in directions:
                                nx, ny = x + dx, y + dy

                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 0:
                                        frontier.add((nx, ny))
                                        wall_count += 1
                                    elif isInfected[nx][ny] == 1 and not visited[nx][ny]:
                                        visited[nx][ny] = True
                                        stack.append((nx, ny))

                        regions.append(region)
                        frontiers.append(frontier)
                        walls.append(wall_count)

            if not regions:
                break

            most_dangerous = max(range(len(frontiers)), key=lambda i: len(frontiers[i]))

            if not frontiers[most_dangerous]:
                break

            total_walls += walls[most_dangerous]

            for r, c in regions[most_dangerous]:
                isInfected[r][c] = -1

            for i, frontier in enumerate(frontiers):
                if i == most_dangerous:
                    continue

                for r, c in frontier:
                    isInfected[r][c] = 1

        return total_walls