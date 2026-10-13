from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals):
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        values = [x[0] for x in starts]
        result = []

        for _, end in intervals:
            idx = bisect_left(values, end)
            result.append(starts[idx][1] if idx < len(starts) else -1)

        return result