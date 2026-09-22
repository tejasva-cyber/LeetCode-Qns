class Solution:
    def diffWaysToCompute(self, expression):
        memo = {}

        def solve(expr):
            if expr in memo:
                return memo[expr]

            result = []

            for i, char in enumerate(expr):
                if char in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i + 1:])

                    for a in left:
                        for b in right:
                            if char == "+":
                                result.append(a + b)
                            elif char == "-":
                                result.append(a - b)
                            else:
                                result.append(a * b)

            if not result:
                result.append(int(expr))

            memo[expr] = result
            return result

        return solve(expression)