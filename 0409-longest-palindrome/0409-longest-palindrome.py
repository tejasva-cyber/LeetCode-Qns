from collections import Counter

class Solution:
    def longestPalindrome(self, s):
        count = Counter(s)
        length = 0
        odd_found = False

        for freq in count.values():
            length += (freq // 2) * 2
            if freq % 2:
                odd_found = True

        return length + odd_found