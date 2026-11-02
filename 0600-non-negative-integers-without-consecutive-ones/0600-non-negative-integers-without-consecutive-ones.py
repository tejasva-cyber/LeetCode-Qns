class Solution:
    def findIntegers(self, n):
        fib = [0] * 32
        fib[0], fib[1] = 1, 2

        for i in range(2, 32):
            fib[i] = fib[i - 1] + fib[i - 2]

        result = 0
        previous = 0

        for i in range(30, -1, -1):
            if n & (1 << i):
                result += fib[i]

                if previous:
                    return result

                previous = 1
            else:
                previous = 0

        return result + 1