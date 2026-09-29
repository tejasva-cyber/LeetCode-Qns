class Solution:
    def palindromePairs(self, words):
        result = []
        word_map = {word: i for i, word in enumerate(words)}

        def is_palindrome(s):
            return s == s[::-1]

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left = word[:j]
                right = word[j:]

                if is_palindrome(left):
                    reversed_right = right[::-1]

                    if reversed_right in word_map and word_map[reversed_right] != i:
                        result.append([word_map[reversed_right], i])

                if j != len(word) and is_palindrome(right):
                    reversed_left = left[::-1]

                    if reversed_left in word_map and word_map[reversed_left] != i:
                        result.append([i, word_map[reversed_left]])

        return result