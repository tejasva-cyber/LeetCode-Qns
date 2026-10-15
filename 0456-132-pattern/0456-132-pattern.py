class Solution:
    def find132pattern(self, nums):
        stack = []
        middle = float("-inf")

        for num in reversed(nums):
            if num < middle:
                return True

            while stack and stack[-1] < num:
                middle = stack.pop()

            stack.append(num)

        return False