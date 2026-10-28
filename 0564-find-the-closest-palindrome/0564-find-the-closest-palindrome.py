class Solution:
    def nearestPalindromic(self, n):
        length = len(n)
        num = int(n)
        prefix = int(n[:(length + 1) // 2])

        candidates = {
            10**length + 1,
            10**(length - 1) - 1
        }

        for p in (prefix - 1, prefix, prefix + 1):
            left = str(p)
            if length % 2:
                palindrome = left + left[:-1][::-1]
            else:
                palindrome = left + left[::-1]
            candidates.add(int(palindrome))

        candidates.discard(num)
        return str(min(candidates, key=lambda x: (abs(x - num), x)))