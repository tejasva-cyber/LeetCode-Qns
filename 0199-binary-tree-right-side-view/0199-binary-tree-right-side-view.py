import collections

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                # Capture the LAST node in the level queue, not the first
                if i == level_size - 1:
                    result.append(node.val)

        return result