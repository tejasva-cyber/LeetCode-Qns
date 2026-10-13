from collections import defaultdict

class Solution:
    def pathSum(self, root, targetSum):
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, current):
            if not node:
                return 0

            current += node.val
            result = prefix[current - targetSum]

            prefix[current] += 1
            result += dfs(node.left, current)
            result += dfs(node.right, current)
            prefix[current] -= 1

            return result

        return dfs(root, 0)