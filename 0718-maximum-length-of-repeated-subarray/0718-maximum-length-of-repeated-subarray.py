class Solution:
    def findLength(self, nums1, nums2):
        dp = [0] * (len(nums2) + 1)
        answer = 0

        for a in nums1:
            for j in range(len(nums2) - 1, -1, -1):
                if a == nums2[j]:
                    dp[j + 1] = dp[j] + 1
                    answer = max(answer, dp[j + 1])
                else:
                    dp[j + 1] = 0

        return answer