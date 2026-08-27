class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        maximum = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    maximum = max(maximum, i - stack[-1])

        return maximum