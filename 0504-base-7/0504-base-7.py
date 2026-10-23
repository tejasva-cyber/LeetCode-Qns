class Solution:
    def convertToBase7(self, num):
        return str(num) if num == 0 else (
            ("-" if num < 0 else "") +
            self.convertToBase7(abs(num))
            if num < 0 else self._convert(num)
        )

    def _convert(self, num):
        result = ""
        while num:
            result = str(num % 7) + result
            num //= 7
        return result