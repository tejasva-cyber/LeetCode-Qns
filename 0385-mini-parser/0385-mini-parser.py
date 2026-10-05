class Solution:
    def deserialize(self, s):
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = 0
        sign = 1
        has_num = False

        for i, ch in enumerate(s):
            if ch == '-':
                sign = -1

            elif ch.isdigit():
                num = num * 10 + int(ch)
                has_num = True

            elif ch == '[':
                stack.append(NestedInteger())

            elif ch in ',]':
                if has_num:
                    stack[-1].add(NestedInteger(sign * num))
                    num = 0
                    sign = 1
                    has_num = False

                if ch == ']' and len(stack) > 1:
                    item = stack.pop()
                    stack[-1].add(item)

        return stack[0]