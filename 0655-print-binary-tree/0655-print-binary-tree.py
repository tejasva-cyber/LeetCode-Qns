class Solution:
    def printTree(self, root):
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        h = height(root)
        width = (1 << h) - 1
        result = [[""] * width for _ in range(h)]

        def fill(node, row, left, right):
            if not node:
                return

            mid = (left + right) // 2
            result[row][mid] = str(node.val)

            fill(node.left, row + 1, left, mid - 1)
            fill(node.right, row + 1, mid + 1, right)

        fill(root, 0, 0, width - 1)
        return result