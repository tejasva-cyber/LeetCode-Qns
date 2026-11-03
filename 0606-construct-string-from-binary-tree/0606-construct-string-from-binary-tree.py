class Solution:
    def tree2str(self, root):
        if not root:
            return ""

        if not root.left and not root.right:
            return str(root.val)

        if not root.right:
            return f"{root.val}({self.tree2str(root.left)})"

        return (
            f"{root.val}({self.tree2str(root.left)})"
            f"({self.tree2str(root.right)})"
        )