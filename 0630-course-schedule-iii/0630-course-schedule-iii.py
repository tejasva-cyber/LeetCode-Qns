import heapq

class Solution:
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x: x[1])
        heap = []
        total = 0

        for duration, deadline in courses:
            total += duration
            heapq.heappush(heap, -duration)

            if total > deadline:
                total += heapq.heappop(heap)

        return len(heap)