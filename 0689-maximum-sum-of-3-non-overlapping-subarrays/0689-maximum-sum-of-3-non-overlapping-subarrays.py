class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        window_count = n - k + 1

        sums = [0] * window_count
        current = sum(nums[:k])
        sums[0] = current

        for i in range(1, window_count):
            current += nums[i + k - 1] - nums[i - 1]
            sums[i] = current

        left = [0] * window_count
        best = 0

        for i in range(window_count):
            if sums[i] > sums[best]:
                best = i
            left[i] = best

        right = [0] * window_count
        best = window_count - 1

        for i in range(window_count - 1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best

        answer = [-1, -1, -1]
        maximum = 0

        for mid in range(k, window_count - k):
            l = left[mid - k]
            r = right[mid + k]
            total = sums[l] + sums[mid] + sums[r]

            if total > maximum:
                maximum = total
                answer = [l, mid, r]

        return answer