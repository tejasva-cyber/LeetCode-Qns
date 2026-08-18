class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        clones = {}

        def dfs(current):
            if current in clones:
                return clones[current]

            clones[current] = Node(current.val)

            for neighbor in current.neighbors:
                clones[current].neighbors.append(dfs(neighbor))

            return clones[current]

        return dfs(node)