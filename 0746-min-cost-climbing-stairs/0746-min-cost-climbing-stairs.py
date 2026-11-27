class Solution:
    def minCostClimbingStairs(self, cost):
        a = b = 0

        for i in range(2, len(cost) + 1):
            a, b = b, min(a + cost[i - 2], b + cost[i - 1])

        return b