class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)
        memo = {}

        def can_build(word):
            if word in memo:
                return memo[word]

            dp = [False] * (len(word) + 1)
            dp[0] = True

            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        dp[i] = True
                        break

            memo[word] = dp[-1]
            return dp[-1]

        result = []

        for word in sorted(words, key=len):
            word_set.remove(word)

            if can_build(word):
                result.append(word)

            word_set.add(word)

        return result