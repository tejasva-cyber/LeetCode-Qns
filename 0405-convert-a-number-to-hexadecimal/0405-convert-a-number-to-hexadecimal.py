class Solution:
    def toHex(self, num):
        if num == 0:
            return "0"

        if num < 0:
            num += 2**32

        digits = "0123456789abcdef"
        result = []

        while num:
            result.append(digits[num & 15])
            num >>= 4

        return ''.join(result[::-1])