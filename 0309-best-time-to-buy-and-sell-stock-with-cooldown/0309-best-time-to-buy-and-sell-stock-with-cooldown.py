class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        hold = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:
            previous_hold = hold
            previous_sold = sold
            previous_rest = rest

            hold = max(previous_hold, previous_rest - price)
            sold = previous_hold + price
            rest = max(previous_rest, previous_sold)

        return max(sold, rest)