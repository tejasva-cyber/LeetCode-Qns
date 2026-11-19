from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)

        return [
            word for word, _ in sorted(
                count.items(),
                key=lambda item: (-item[1], item[0])
            )[:k]
        ]