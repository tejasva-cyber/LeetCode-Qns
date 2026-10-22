class Solution:
    def smallestGoodBase(self, n):
        n = int(n)

        for length in range(n.bit_length(), 1, -1):
            low, high = 2, int(n ** (1 / (length - 1))) + 1

            while low <= high:
                base = (low + high) // 2
                total = 1
                term = 1

                for _ in range(length - 1):
                    term *= base
                    total += term

                if total == n:
                    return str(base)
                elif total < n:
                    low = base + 1
                else:
                    high = base - 1

        return str(n - 1)