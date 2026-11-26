class Solution:
    def evaluate(self, expression):
        def parse(expr, env):
            if expr[0] != '(':
                if expr.lstrip('-').isdigit():
                    return int(expr)
                return env[expr]

            expr = expr[1:-1]

            if expr.startswith('add '):
                parts = self.split_expr(expr[4:])
                return parse(parts[0], env) + parse(parts[1], env)

            if expr.startswith('mult '):
                parts = self.split_expr(expr[5:])
                return parse(parts[0], env) * parse(parts[1], env)

            parts = self.split_expr(expr[4:])
            local = env.copy()

            for i in range(0, len(parts) - 1, 2):
                local[parts[i]] = parse(parts[i + 1], local)

            return parse(parts[-1], local)

        return parse(expression, {})

    def split_expr(self, expr):
        parts = []
        depth = 0
        start = 0

        for i, char in enumerate(expr):
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            elif char == ' ' and depth == 0:
                parts.append(expr[start:i])
                start = i + 1

        parts.append(expr[start:])
        return parts