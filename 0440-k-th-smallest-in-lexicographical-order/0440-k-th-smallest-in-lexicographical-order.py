class Solution:
    def findKthNumber(self, n, k):
        current = 1
        k -= 1

        while k > 0:
            steps = 0
            first = current
            next_num = current + 1

            while first <= n:
                steps += min(n + 1, next_num) - first
                first *= 10
                next_num *= 10

            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1

        return current