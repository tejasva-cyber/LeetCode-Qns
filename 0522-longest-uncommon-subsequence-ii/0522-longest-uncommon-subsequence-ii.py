class Solution:
    def findLUSlength(self, strs):
        def is_subsequence(a, b):
            i = 0

            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1

            return i == len(a)

        for i, word in sorted(
            enumerate(strs),
            key=lambda x: len(x[1]),
            reverse=True
        ):
            if all(
                i == j or not is_subsequence(word, other)
                for j, other in enumerate(strs)
            ):
                return len(word)

        return -1