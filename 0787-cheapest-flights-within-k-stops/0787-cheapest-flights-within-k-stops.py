import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = [[] for _ in range(n)]

        for u, v, price in flights:
            graph[u].append((v, price))

        heap = [(0, src, 0)]
        best = {}

        while heap:
            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost

            if stops > k:
                continue

            if (city, stops) in best and best[(city, stops)] <= cost:
                continue

            best[(city, stops)] = cost

            for next_city, price in graph[city]:
                heapq.heappush(
                    heap,
                    (cost + price, next_city, stops + 1)
                )

        return -1