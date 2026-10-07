class Solution:
    def findTheDifference(self, s, t):
        result = 0

        for ch in s + t:
            result ^= ord(ch)

        return chr(result)