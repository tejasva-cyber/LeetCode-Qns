from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(cur, target, visited):
            if cur == target:
                return 1.0

            visited.add(cur)

            for nxt, weight in graph[cur]:
                if nxt in visited:
                    continue

                result = dfs(nxt, target, visited)

                if result != -1:
                    return weight * result

            return -1.0

        return [
            dfs(a, b, set()) if a in graph and b in graph else -1.0
            for a, b in queries
        ]