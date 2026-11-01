from fractions import Fraction

class Solution:
    def fractionAddition(self, expression):
        import re

        result = Fraction(0, 1)

        for part in re.findall(r'[+-]?\d+/\d+', expression):
            numerator, denominator = map(int, part.split('/'))
            result += Fraction(numerator, denominator)

        return f"{result.numerator}/{result.denominator}"