from functools import lru_cache

class Solution:
    def shoppingOffers(self, price, special, needs):
        n = len(price)
        valid = []

        for offer in special:
            if sum(offer[i] for i in range(n)) > 0:
                if sum(offer[i] * price[i] for i in range(n)) > offer[-1]:
                    valid.append(offer)

        @lru_cache(None)
        def dfs(remaining):
            cost = sum(remaining[i] * price[i] for i in range(n))

            for offer in valid:
                new_needs = []
                for i in range(n):
                    if offer[i] > remaining[i]:
                        break
                    new_needs.append(remaining[i] - offer[i])
                else:
                    cost = min(
                        cost,
                        offer[-1] + dfs(tuple(new_needs))
                    )

            return cost

        return dfs(tuple(needs))