class Solution:
    def longestWord(self, words):
        word_set = set(words)
        answer = ""

        for word in sorted(words):
            if all(word[:i] in word_set for i in range(1, len(word))):
                if len(word) > len(answer):
                    answer = word

        return answer