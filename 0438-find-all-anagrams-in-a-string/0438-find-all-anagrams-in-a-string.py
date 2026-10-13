from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        need = Counter(p)
        window = Counter(s[:len(p)])
        result = []

        if window == need:
            result.append(0)

        for i in range(len(p), len(s)):
            window[s[i]] += 1
            left_char = s[i - len(p)]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            if window == need:
                result.append(i - len(p) + 1)

        return result