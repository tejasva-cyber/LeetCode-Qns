class Solution:
    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        if k:
            stack = stack[:-k]

        result = ''.join(stack).lstrip('0')

        return result or "0"