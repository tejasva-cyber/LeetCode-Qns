class Solution:
    def countOfAtoms(self, formula: str) -> str:
        from collections import Counter

class Solution:
    def countOfAtoms(self, formula):
        stack = [Counter()]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1

            elif formula[i] == ')':
                group = stack.pop()
                i += 1
                start = i

                while i < n and formula[i].isdigit():
                    i += 1

                multiplier = int(formula[start:i] or 1)

                for atom, count in group.items():
                    stack[-1][atom] += count * multiplier

            else:
                start = i
                i += 1

                while i < n and formula[i].islower():
                    i += 1

                atom = formula[start:i]
                start = i

                while i < n and formula[i].isdigit():
                    i += 1

                count = int(formula[start:i] or 1)
                stack[-1][atom] += count

        return ''.join(
            atom + (str(count) if count > 1 else '')
            for atom, count in sorted(stack[0].items())
        )