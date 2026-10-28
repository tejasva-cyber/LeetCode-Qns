class Solution:
    def intersect(self, quadTree1, quadTree2):
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2

        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1

        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        if (topLeft.isLeaf and topRight.isLeaf and
            bottomLeft.isLeaf and bottomRight.isLeaf and
            topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            return Node(topLeft.val, True, None, None, None, None)

        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)