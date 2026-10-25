class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for value in range(coin, amount + 1):
                dp[value] += dp[value - coin]

        return dp[amount]