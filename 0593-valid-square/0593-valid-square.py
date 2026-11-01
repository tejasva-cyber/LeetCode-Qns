class Solution:
    def validSquare(self, p1, p2, p3, p4):
        points = [p1, p2, p3, p4]

        distances = sorted(
            (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
            for i, a in enumerate(points)
            for b in points[i + 1:]
        )

        return (
            distances[0] > 0
            and distances[0] == distances[1] == distances[2] == distances[3]
            and distances[4] == distances[5] == 2 * distances[0]
        )