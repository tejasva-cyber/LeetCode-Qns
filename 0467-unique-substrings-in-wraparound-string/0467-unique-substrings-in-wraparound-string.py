class Solution:
    def findSubstringInWraproundString(self, s):
        longest = [0] * 26
        length = 0

        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1])) % 26 == 1:
                length += 1
            else:
                length = 1

            idx = ord(ch) - ord('a')
            longest[idx] = max(longest[idx], length)

        return sum(longest)