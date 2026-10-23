class Solution:
    def findMode(self, root):
        from collections import Counter

        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        count = Counter(values)
        maximum = max(count.values())

        return [x for x, freq in count.items() if freq == maximum]