class Solution:
    def largestValues(self, root):
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            result.append(max(node.val for node in queue))
            next_level = []

            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            queue = next_level

        return result