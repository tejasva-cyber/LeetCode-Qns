class Solution:
    def addOneRow(self, root, val, depth):
        if depth == 1:
            from_tree = TreeNode(val)
            from_tree.left = root
            return from_tree

        def dfs(node, level):
            if not node:
                return

            if level == depth - 1:
                old_left = node.left
                old_right = node.right

                node.left = TreeNode(val)
                node.right = TreeNode(val)

                node.left.left = old_left
                node.right.right = old_right
                return

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)
        return root