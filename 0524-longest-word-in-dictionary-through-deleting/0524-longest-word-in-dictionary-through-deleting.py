class Solution:
    def findLongestWord(self, s, dictionary):
        def is_subsequence(word):
            i = 0

            for ch in s:
                if i < len(word) and word[i] == ch:
                    i += 1

            return i == len(word)

        answer = ""

        for word in dictionary:
            if is_subsequence(word):
                if len(word) > len(answer):
                    answer = word
                elif len(word) == len(answer) and word < answer:
                    answer = word

        return answer