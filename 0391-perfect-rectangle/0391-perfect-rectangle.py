class Solution:
    def isRectangleCover(self, rectangles):
        area = 0
        corners = set()

        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)

            for p in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)

        xs = [r[0] for r in rectangles] + [r[2] for r in rectangles]
        ys = [r[1] for r in rectangles] + [r[3] for r in rectangles]

        bounding_area = (max(xs) - min(xs)) * (max(ys) - min(ys))

        expected = {
            (min(xs), min(ys)),
            (min(xs), max(ys)),
            (max(xs), min(ys)),
            (max(xs), max(ys))
        }

        return area == bounding_area and corners == expected