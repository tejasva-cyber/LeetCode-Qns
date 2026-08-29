class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    # int(float()) forces truncation towards zero instead of flooring towards negative infinity
                    stack.append(int(float(a) / b))
            else:
                stack.append(int(token))
        return stack[-1]