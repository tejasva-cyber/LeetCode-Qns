class Codec:
    def serialize(self, root):
        values = []

        def preorder(node):
            if node:
                values.append(str(node.val))
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return ",".join(values)

    def deserialize(self, data):
        if not data:
            return None

        values = iter(map(int, data.split(",")))

        def build(low, high):
            nonlocal_value = None

            try:
                value = next(values)
            except StopIteration:
                return None

            if not low < value < high:
                return None

            node = TreeNode(value)
            node.left = build(low, value)
            node.right = build(value, high)
            return node

        # Use an index-based preorder parser.
        vals = list(map(int, data.split(",")))
        index = 0

        def construct(low, high):
            nonlocal index

            if index == len(vals) or not low < vals[index] < high:
                return None

            value = vals[index]
            index += 1

            node = TreeNode(value)
            node.left = construct(low, value)
            node.right = construct(value, high)
            return node

        return construct(float("-inf"), float("inf"))