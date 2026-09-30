class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        heights = [h for _, h in envelopes]
        dp = []

        for h in heights:
            left, right = 0, len(dp)

            while left < right:
                mid = (left + right) // 2

                if dp[mid] < h:
                    left = mid + 1
                else:
                    right = mid

            if left == len(dp):
                dp.append(h)
            else:
                dp[left] = h

        return len(dp)