from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root):
        if not root:
            return []

        counts = Counter()

        def dfs(node):
            if not node:
                return 0

            total = node.val + dfs(node.left) + dfs(node.right)
            counts[total] += 1
            return total

        dfs(root)
        maximum = max(counts.values())

        return [s for s, count in counts.items() if count == maximum]