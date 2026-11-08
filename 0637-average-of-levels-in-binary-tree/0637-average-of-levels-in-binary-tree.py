from collections import deque

class Solution:
    def averageOfLevels(self, root):
        queue = deque([root])
        result = []

        while queue:
            total = 0
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                total += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(total / size)

        return result