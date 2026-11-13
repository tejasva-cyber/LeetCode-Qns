from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        queue = deque([(root, 0)])
        maximum = 0

        while queue:
            level_length = len(queue)
            first = queue[0][1]
            last = 0

            for _ in range(level_length):
                node, index = queue.popleft()
                index -= first
                last = index

                if node.left:
                    queue.append((node.left, 2 * index))

                if node.right:
                    queue.append((node.right, 2 * index + 1))

            maximum = max(maximum, last + 1)

        return maximum