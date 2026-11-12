class Solution:
    def findDuplicateSubtrees(self, root):
        from collections import defaultdict

        count = defaultdict(int)
        result = []

        def serialize(node):
            if not node:
                return "#"

            key = (
                str(node.val) + "," +
                serialize(node.left) + "," +
                serialize(node.right)
            )

            count[key] += 1

            if count[key] == 2:
                result.append(node)

            return key

        serialize(root)
        return result