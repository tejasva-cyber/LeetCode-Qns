class Solution:
    def solveEquation(self, equation):
        left, right = equation.split('=')

        def parse(expr):
            x = 0
            const = 0
            expr = expr.replace('-', '+-')

            for term in expr.split('+'):
                if not term:
                    continue

                if 'x' in term:
                    value = term.replace('x', '')
                    x += int(value) if value not in ('', '+', '-') else (
                        -1 if value == '-' else 1
                    )
                else:
                    const += int(term)

            return x, const

        a, b = parse(left)
        c, d = parse(right)

        coefficient = a - c
        constant = d - b

        if coefficient == 0:
            return "Infinite solutions" if constant == 0 else "No solution"

        return f"x={constant // coefficient}"