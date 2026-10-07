class Solution:
    def decodeString(self, s):
        stack = []
        num = 0
        cur = ""

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                stack.append((cur, num))
                cur = ""
                num = 0

            elif ch == ']':
                prev, count = stack.pop()
                cur = prev + cur * count

            else:
                cur += ch

        return cur