class Solution:
    def maxProduct(self, words):
        masks = []
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            masks.append(mask)

        result = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if masks[i] & masks[j] == 0:
                    result = max(result, len(words[i]) * len(words[j]))

        return result