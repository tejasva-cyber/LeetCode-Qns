class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None

        maximum = max(nums)
        index = nums.index(maximum)

        root = TreeNode(maximum)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index + 1:])

        return root