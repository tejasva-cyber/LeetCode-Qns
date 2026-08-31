from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        target = Counter(words)
        result = []

        for start in range(word_len):
            left = start
            count = 0
            window = Counter()

            for right in range(start, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word not in target:
                    window.clear()
                    count = 0
                    left = right + word_len
                    continue

                window[word] += 1
                count += 1

                while window[word] > target[word]:
                    removed = s[left:left + word_len]
                    window[removed] -= 1
                    left += word_len
                    count -= 1

                if count == len(words):
                    result.append(left)

                    removed = s[left:left + word_len]
                    window[removed] -= 1
                    left += word_len
                    count -= 1

        return result