class Solution:
    def hasAlternatingBits(self, n):
        bits = n ^ (n >> 1)
        return (bits & (bits + 1)) == 0