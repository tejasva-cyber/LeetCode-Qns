class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))
        candidate1 = candidate2 = None

        for u, v in edges:
            if parent[v] != v:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
                break
            parent[v] = u

        def find_root(edges_to_use):
            parent = list(range(n + 1))

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            for u, v in edges_to_use:
                ru, rv = find(u), find(v)

                if ru == rv:
                    return [u, v]

                parent[ru] = rv

            return None

        if candidate2:
            filtered = [e for e in edges if e != candidate2]
            if find_root(filtered) is None:
                return candidate2
            return candidate1

        return find_root(edges)