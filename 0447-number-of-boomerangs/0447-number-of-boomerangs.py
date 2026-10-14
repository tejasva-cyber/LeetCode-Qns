from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points):
        result = 0

        for x1, y1 in points:
            distances = defaultdict(int)

            for x2, y2 in points:
                dx, dy = x1 - x2, y1 - y2
                distances[dx * dx + dy * dy] += 1

            for count in distances.values():
                result += count * (count - 1)

        return result