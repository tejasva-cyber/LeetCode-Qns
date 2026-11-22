class Solution(object):
    def findShortestSubArray(self, nums):
        if not nums:
            return 0

        first = {}
        count = {}
        max_freq = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
                curr = 1
            else:
                curr = count[num] + 1

            count[num] = curr

            # New highest frequency resets the shortest valid span
            if curr > max_freq:
                max_freq = curr
                min_len = i - first[num] + 1
            # Tie in frequency keeps the tightest window
            elif curr == max_freq:
                span = i - first[num] + 1
                if span < min_len:
                    min_len = span

        return min_len