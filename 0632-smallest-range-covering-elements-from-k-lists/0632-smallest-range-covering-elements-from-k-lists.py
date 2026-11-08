import heapq

class Solution:
    def smallestRange(self, nums):
        heap = []
        current_max = float('-inf')

        for i, arr in enumerate(nums):
            heapq.heappush(heap, (arr[0], i, 0))
            current_max = max(current_max, arr[0])

        best_range = [float('-inf'), float('inf')]

        while heap:
            current_min, i, j = heapq.heappop(heap)

            if current_max - current_min < best_range[1] - best_range[0]:
                best_range = [current_min, current_max]

            if j + 1 == len(nums[i]):
                break

            next_value = nums[i][j + 1]
            heapq.heappush(heap, (next_value, i, j + 1))
            current_max = max(current_max, next_value)

        return best_range