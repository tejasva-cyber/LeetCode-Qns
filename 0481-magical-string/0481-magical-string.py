class Solution:
    def magicalString(self, n):
        if n <= 0:
            return 0

        s = [1, 2, 2]
        i = 2
        next_num = 1

        while len(s) < n:
            s.extend([next_num] * s[i])
            next_num = 3 - next_num
            i += 1

        return s[:n].count(1)