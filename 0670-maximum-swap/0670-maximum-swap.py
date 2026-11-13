class Solution:
    def maximumSwap(self, num):
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}

        for i, digit in enumerate(digits):
            for d in range(9, int(digit), -1):
                if d in last and last[d] > i:
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    return int(''.join(digits))

        return num