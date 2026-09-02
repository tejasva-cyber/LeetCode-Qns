class Solution:
    def getPermutation(self, n, k):
        import math

        numbers = list(range(1, n + 1))
        result = []
        k -= 1

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            k %= fact
            result.append(str(numbers.pop(index)))

        return ''.join(result)