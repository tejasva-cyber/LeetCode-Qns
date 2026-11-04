from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        counts = Counter(tasks)
        maximum = max(counts.values())
        max_count = sum(v == maximum for v in counts.values())

        return max(
            len(tasks),
            (maximum - 1) * (n + 1) + max_count
        )