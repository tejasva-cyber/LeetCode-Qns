class Solution:
    def lengthLongestPath(self, input):
        stack = [0]
        ans = 0

        for line in input.split('\n'):
            depth = line.count('\t')
            name = line.lstrip('\t')

            while len(stack) > depth + 1:
                stack.pop()

            length = stack[-1] + len(name) + 1

            if '.' in name:
                ans = max(ans, length - 1)
            else:
                stack.append(length)

        return ans