class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])

        count = 0
        current_end = float('-inf')

        for start, end in pairs:
            if start > current_end:
                count += 1
                current_end = end

        return count