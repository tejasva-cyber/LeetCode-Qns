class Solution(object):
    def minCut(self, s):
        n = len(s)
        if n <= 1:
            return 0
            
        # dp[i] tracks the minimum cuts needed for the substring s[0...i]
        dp = [i for i in range(n)]
        
        for i in range(n):
            # Phase 1: Expand odd-length palindromes (center is at i)
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left - 1] + 1)
                left -= 1
                right += 1
                
            # Phase 2: Expand even-length palindromes (center is between i and i+1)
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left - 1] + 1)
                left -= 1
                right += 1
                
        return dp[-1]